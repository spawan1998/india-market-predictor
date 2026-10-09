"""Command-line interface.

    imp predict  [--symbol NIFTY50] [--horizon 5] [--model gbm]
    imp backtest [--symbol NIFTY50] [--horizon 5] [--threshold 0.55] [--cost-bps 20]
    imp scan     [--capital 200000] [--risk 1.0] [--top 10]
    imp size     --entry 1500 --atr 30 --capital 200000 [--risk 1]
    imp report   [--symbol NIFTY50]       # predict + backtest + scan -> reports/
    imp update                            # refresh the data cache
"""
from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

import pandas as pd
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from . import backtest as bt
from . import model as mdl
from .data import fetch, fetch_context, fetch_many
from .report import REPORT_DIR, equity_chart, importance_chart, price_chart, write_markdown
from .scan import position_size, scan
from .universe import NIFTY50, display_name, to_yahoo

console = Console()

DISCLAIMER = (
    "Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. "
    "A probability is a lean, not a forecast. Risk only what the position-size rule allows."
)


def _pct(x: float) -> str:
    return "n/a" if pd.isna(x) else f"{x * 100:+.1f}%"


def _load(symbol: str, refresh: bool):
    df = fetch(symbol, refresh=refresh)
    ticker = to_yahoo(symbol)
    ctx = fetch_context(refresh=refresh) if ticker.startswith("^") else fetch_context(refresh=refresh)
    # For single stocks, context still helps (market beta), so keep it.
    return df, ctx


def _evaluate(symbol: str, horizon: int, kind: str, refresh: bool):
    df, ctx = _load(symbol, refresh)
    X, y, fwd = mdl.prepare(df, ctx, horizon)
    probs, res = mdl.walk_forward(X, y, kind=kind, horizon=horizon)
    full = mdl.fit_full(X, y, kind=kind, horizon=horizon)
    p_latest = float(full.predict_proba(X.iloc[[-1]])[:, 1][0])
    return df, X, y, probs, res, full, p_latest


# ---------- commands ----------

def cmd_predict(a):
    df, X, y, probs, res, full, p = _evaluate(a.symbol, a.horizon, a.model, a.refresh)
    name = display_name(to_yahoo(a.symbol))
    last = df.index[-1].date()
    stance = mdl.describe_probability(p)
    recent = probs.dropna().iloc[-10:]

    console.print(Panel.fit(
        f"[bold]{name}[/bold]  close {df['Close'].iloc[-1]:,.2f} on {last}\n"
        f"P(up over next {a.horizon} sessions) = [bold]{p:.3f}[/bold]  ->  {stance}\n\n"
        f"Walk-forward (out-of-sample, {res.n_predictions} predictions, {res.n_retrains} retrains):\n"
        f"  accuracy {res.accuracy:.3f}   balanced {res.balanced_accuracy:.3f}   AUC {res.auc:.3f}\n"
        f"  'always up' baseline {res.baseline_always_up:.3f}\n\n"
        f"Last 10 out-of-sample probabilities: " + " ".join(f"{v:.2f}" for v in recent),
        title=f"imp predict ({a.model}, horizon {a.horizon})", border_style="blue"))
    console.print(_edge_note(res))
    sma200 = df["Close"].rolling(200).mean().iloc[-1]
    console.print(f"Trend filter: close is {'ABOVE' if df['Close'].iloc[-1] > sma200 else 'BELOW'} the 200-day SMA ({sma200:,.0f}).")
    console.print(f"[dim]{DISCLAIMER}[/dim]")
    if a.save:
        p_ = mdl.save(full, f"{name}_h{a.horizon}_{a.model}")
        console.print(f"model saved to {p_}")


def _edge_note(res) -> str:
    if pd.isna(res.auc) or res.auc < 0.53:
        return ("[yellow]No proven edge on this symbol: out-of-sample AUC is ~0.5, so the probability above is "
                "closer to noise than to a forecast. The honest baseline is 'always up' or the SMA-200 trend filter.[/yellow]")
    return "[green]Model shows a small out-of-sample edge (AUC >= 0.53). Still size positions by risk, not conviction.[/green]"


def _stats_table(stats, title: str) -> Table:
    t = Table(title=title)
    t.add_column("metric")
    for s in stats:
        t.add_column(s.name, justify="right")
    rows = [("total return", lambda s: _pct(s.total_return)), ("CAGR", lambda s: _pct(s.cagr)),
            ("Sharpe", lambda s: f"{s.sharpe:.2f}"), ("max drawdown", lambda s: _pct(s.max_drawdown)),
            ("time in market", lambda s: _pct(s.time_in_market).lstrip("+")), ("switches", lambda s: str(s.n_trades)),
            ("hit rate (days held)", lambda s: _pct(s.hit_rate).lstrip("+"))]
    for label, fn in rows:
        t.add_row(label, *[fn(s) for s in stats])
    return t


def cmd_backtest(a):
    df, X, y, probs, res, full, p = _evaluate(a.symbol, a.horizon, a.model, a.refresh)
    name = display_name(to_yahoo(a.symbol))
    stats, curves = bt.compare(df["Close"], probs, a.threshold, a.hysteresis, a.cost_bps)
    console.print(_stats_table(stats, f"{name}: out-of-sample {curves.index[0].date()} to {curves.index[-1].date()}, "
                                      f"{a.cost_bps} bps per switch, ml enters >{a.threshold} exits <{a.threshold - a.hysteresis:.2f}"))
    console.print(_edge_note(res))

    sweep = bt.threshold_sweep(df["Close"], probs, a.cost_bps, a.hysteresis)
    t2 = Table(title="threshold sweep (pick for robustness, not the single best row)")
    for col in sweep.columns:
        t2.add_column(col, justify="right")
    for _, row in sweep.iterrows():
        t2.add_row(f"{row.threshold:.2f}", _pct(row.cagr), f"{row.sharpe:.2f}", _pct(row.max_dd),
                   str(int(row.trades)), _pct(row.time_in_mkt).lstrip("+"))
    console.print(t2)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    out = equity_chart(curves, name, REPORT_DIR / f"{name}_equity.png")
    console.print(f"equity curve -> {out}")
    console.print(f"[dim]{DISCLAIMER}[/dim]")


def cmd_scan(a):
    df = scan(refresh=a.refresh)
    nifty3m = df.attrs.get("nifty_ret_3m", float("nan"))
    t = Table(title=f"NIFTY 50 swing scan  (NIFTY 3m {_pct(nifty3m)}; score 0-5, higher = stronger trend/momentum)")
    for col in ("symbol", "close", "score", "rsi14", "ret_1m", "rel_3m", "vs_sma50", "vs_sma200", "from_20d_high", "atr_pct"):
        t.add_column(col, justify="right" if col != "symbol" else "left")
    for _, r in df.head(a.top).iterrows():
        t.add_row(r.symbol, f"{r.close:,.1f}", f"{r.score:.1f}", f"{r.rsi14:.0f}", _pct(r.ret_1m), _pct(r.rel_3m),
                  _pct(r.vs_sma50), _pct(r.vs_sma200), _pct(r.from_20d_high), f"{r.atr_pct*100:.1f}%")
    console.print(t)

    if a.capital:
        t2 = Table(title=f"position size for top {min(a.top, 5)} if bought at close  (capital {a.capital:,.0f}, risk {a.risk}% per trade, stop 2 ATR)")
        for col in ("symbol", "entry", "stop", "target_2R", "qty", "position_value", "rupees_at_risk"):
            t2.add_column(col, justify="right" if col != "symbol" else "left")
        for _, r in df.head(min(a.top, 5)).iterrows():
            s = position_size(r.close, r.atr, a.capital, a.risk)
            t2.add_row(r.symbol, f"{s['entry']:,.1f}", f"{s['stop']:,.1f}", f"{s['target_2R']:,.1f}",
                       str(s["qty"]), f"{s['position_value']:,.0f}", f"{s['rupees_at_risk']:,.0f}")
        console.print(t2)
    if df.attrs.get("missing"):
        console.print(f"[dim]no data for: {', '.join(df.attrs['missing'])}[/dim]")
    console.print("[dim]Weak list (bottom of the ranking) = avoid or short candidates for experienced traders only.[/dim]")


def cmd_size(a):
    s = position_size(a.entry, a.atr, a.capital, a.risk, a.atr_mult)
    for k, v in s.items():
        console.print(f"{k:>16}: {v:,}" if isinstance(v, (int, float)) else f"{k:>16}: {v}")


def cmd_update(a):
    for s in ("NIFTY50", "BANKNIFTY"):
        fetch(s, refresh=True)
    fetch_context(refresh=True)
    got = fetch_many(NIFTY50, refresh=True)
    console.print(f"cache refreshed: indices, context, {len(got)}/{len(NIFTY50)} NIFTY 50 stocks")


def cmd_site(a):
    from .site import APP_DATA, build

    results = build(a.symbols, a.horizon, a.model, a.step, a.workers)
    ok = [r for r in results if "error" not in r]
    bad = [r for r in results if "error" in r]
    console.print(f"site data -> {APP_DATA}: {len(ok)} symbols ok, {len(bad)} failed"
                  + (": " + ", ".join(f"{r['symbol']} ({r['error'][:40]})" for r in bad) if bad else ""))
    if ok:
        console.print("slowest: " + ", ".join(f"{r['symbol']} {r['seconds']}s" for r in sorted(ok, key=lambda r: -r["seconds"])[:3]))


def cmd_report(a):
    today = dt.date.today().isoformat()
    name = display_name(to_yahoo(a.symbol))
    df, X, y, probs, res, full, p = _evaluate(a.symbol, a.horizon, a.model, a.refresh)
    stats, curves = bt.compare(df["Close"], probs, a.threshold, a.hysteresis, a.cost_bps)
    by = {s.name: s for s in stats}
    imp = mdl.feature_importance(full, X, y)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    price_chart(df, probs, name, REPORT_DIR / f"{name}_price.png")
    equity_chart(curves, name, REPORT_DIR / f"{name}_equity.png")
    importance_chart(imp, REPORT_DIR / f"{name}_importance.png")

    sc = scan(refresh=False)
    top = sc.head(10)[["symbol", "close", "score", "rsi14", "ret_1m", "rel_3m", "from_20d_high", "atr_pct"]].copy()
    for c in ("ret_1m", "rel_3m", "from_20d_high", "atr_pct"):
        top[c] = (top[c] * 100).round(1)
    bottom = sc.tail(5)[["symbol", "close", "score", "rsi14", "ret_1m", "rel_3m"]].copy()
    for c in ("ret_1m", "rel_3m"):
        bottom[c] = (bottom[c] * 100).round(1)
    for frame in (top, bottom):
        frame["score"] = frame["score"].round(1)
        frame["rsi14"] = frame["rsi14"].round(0).astype(int)
        frame["close"] = frame["close"].round(2)

    sections = [
        (f"{name} daily read: {today}",
         f"Close **{df['Close'].iloc[-1]:,.2f}** ({df.index[-1].date()}). "
         f"Model P(up over next {a.horizon} sessions) = **{p:.3f}**: {mdl.describe_probability(p)}.\n\n"
         f"![price](./{name}_price.png)"),
        ("How much to trust it",
         f"Walk-forward out-of-sample: accuracy {res.accuracy:.3f}, balanced {res.balanced_accuracy:.3f}, "
         f"AUC {res.auc:.3f}, always-up baseline {res.baseline_always_up:.3f} over {res.n_predictions} predictions. "
         + ("**No proven edge** (AUC ~0.5): treat the probability as noise. " if pd.isna(res.auc) or res.auc < 0.53 else "Small edge (AUC >= 0.53). ")
         + f"Close is {'above' if df['Close'].iloc[-1] > df['Close'].rolling(200).mean().iloc[-1] else 'below'} the 200-day SMA.\n\n"
         + "| strategy | CAGR | max DD | Sharpe | switches |\n|---|---|---|---|---|\n"
         + "\n".join(f"| {s.name} | {_pct(s.cagr)} | {_pct(s.max_drawdown)} | {s.sharpe:.2f} | {s.n_trades} |" for s in stats)
         + f"\n\nCosts {a.cost_bps} bps per switch; ml enters above {a.threshold}, exits below {a.threshold - a.hysteresis:.2f}.\n\n"
         f"![equity](./{name}_equity.png)\n\n![importance](./{name}_importance.png)"),
        ("NIFTY 50 swing scan: strongest", top.to_markdown(index=False)),
        ("NIFTY 50 swing scan: weakest", bottom.to_markdown(index=False)),
        ("Disclaimer", DISCLAIMER),
    ]
    out = write_markdown(REPORT_DIR / f"{today}_{name}.md", sections)
    if name == "NIFTY50":
        write_markdown(REPORT_DIR / "latest.md", sections)
        _write_report_index()
    console.print(f"report -> {out}")


def _write_report_index():
    """reports/index.md: link list of every dated report, newest first (for the website)."""
    dated = sorted(REPORT_DIR.glob("20??-??-??_*.md"), reverse=True)
    lines = ["# Daily reports", "", "[Latest report](./latest.md) is regenerated every weekday after the NSE close.", ""]
    lines += [f"- [{p.stem.replace('_', ' ')}](./{p.name})" for p in dated]
    (REPORT_DIR / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="imp", description="India market predictor (educational)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--symbol", default="NIFTY50", help="NIFTY50, BANKNIFTY, RELIANCE, TCS.NS, ^NSEI ...")
        p.add_argument("--horizon", type=int, default=5, help="sessions ahead (1 = next day, 5 = one week)")
        p.add_argument("--model", choices=["gbm", "logit"], default="gbm")
        p.add_argument("--refresh", action="store_true", help="ignore the cache and re-download")

    p = sub.add_parser("predict", help="probability that price is higher after N sessions"); common(p)
    p.add_argument("--save", action="store_true"); p.set_defaults(fn=cmd_predict)

    p = sub.add_parser("backtest", help="walk-forward long/flat backtest with costs"); common(p)
    p.add_argument("--threshold", type=float, default=0.55); p.add_argument("--cost-bps", type=float, default=20.0)
    p.add_argument("--hysteresis", type=float, default=0.05, help="exit when P(up) < threshold - hysteresis")
    p.set_defaults(fn=cmd_backtest)

    p = sub.add_parser("scan", help="rank NIFTY 50 stocks by trend and momentum")
    p.add_argument("--capital", type=float, default=0, help="rupees; enables position sizing table")
    p.add_argument("--risk", type=float, default=1.0, help="percent of capital risked per trade")
    p.add_argument("--top", type=int, default=10); p.add_argument("--refresh", action="store_true")
    p.set_defaults(fn=cmd_scan)

    p = sub.add_parser("size", help="position size from entry, ATR, capital and risk percent")
    p.add_argument("--entry", type=float, required=True); p.add_argument("--atr", type=float, required=True)
    p.add_argument("--capital", type=float, required=True); p.add_argument("--risk", type=float, default=1.0)
    p.add_argument("--atr-mult", type=float, default=2.0); p.set_defaults(fn=cmd_size)

    p = sub.add_parser("report", help="markdown report with charts in reports/"); common(p)
    p.add_argument("--threshold", type=float, default=0.55); p.add_argument("--cost-bps", type=float, default=20.0)
    p.add_argument("--hysteresis", type=float, default=0.05)
    p.set_defaults(fn=cmd_report)

    p = sub.add_parser("update", help="refresh the price cache"); p.set_defaults(fn=cmd_update)

    p = sub.add_parser("site", help="precompute JSON for the web app (app/data/) for NIFTY, BANKNIFTY and NIFTY 50")
    p.add_argument("--symbols", nargs="*", help="override the symbol list")
    p.add_argument("--horizon", type=int, default=5); p.add_argument("--model", choices=["gbm", "logit"], default="gbm")
    p.add_argument("--step", type=int, default=126, help="walk-forward retrain interval (sessions)")
    p.add_argument("--workers", type=int, default=2)
    p.set_defaults(fn=cmd_site)

    a = ap.parse_args(argv)
    try:
        a.fn(a)
    except RuntimeError as e:
        console.print(f"[red]{e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
