"""Precompute per-symbol predictions as JSON for the static web app in app/.

Runs in the daily GitHub Action. For every symbol it writes
``app/data/<SYMBOL>.json`` (last ~2 years of close, SMA 50/200 and the
out-of-sample P(up), plus the latest probability, walk-forward metrics and
backtest stats) and ``app/data/index.json`` (one row per symbol).
"""
from __future__ import annotations

import json
import math
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import pandas as pd

from . import backtest as bt
from . import model as mdl
from .data import fetch, fetch_context
from .features import sma
from .universe import NIFTY50, display_name, to_yahoo

APP_DATA = Path(__file__).resolve().parent.parent / "app" / "data"
DEFAULT_SYMBOLS = ["NIFTY50", "BANKNIFTY"] + NIFTY50


def _clean(v):
    if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
        return None
    return v


def compute_symbol(symbol: str, horizon: int = 5, kind: str = "gbm", step: int = 126, lookback: int = 500) -> dict:
    df = fetch(symbol)
    ctx = fetch_context()
    X, y, _ = mdl.prepare(df, ctx, horizon)
    if len(X) < 400:
        raise RuntimeError(f"listed too recently ({len(X)} usable sessions; need 400+)")
    probs, res = mdl.walk_forward(X, y, kind=kind, horizon=horizon, step=step)
    full = mdl.fit_full(X, y, kind=kind, horizon=horizon)
    p = float(full.predict_proba(X.iloc[[-1]])[:, 1][0])
    stats, _ = bt.compare(df["Close"], probs, 0.55, 0.05, 20.0)

    tail = df.iloc[-lookback:]
    s50, s200 = sma(df["Close"], 50).iloc[-lookback:], sma(df["Close"], 200).iloc[-lookback:]
    pr = probs.reindex(tail.index)
    name = display_name(to_yahoo(symbol))
    return {
        "symbol": name,
        "yahoo": to_yahoo(symbol),
        "horizon": horizon,
        "model": kind,
        "last_date": str(tail.index[-1].date()),
        "close": round(float(tail["Close"].iloc[-1]), 2),
        "p_up": round(p, 3),
        "stance": mdl.describe_probability(p),
        "above_sma200": bool(tail["Close"].iloc[-1] > s200.iloc[-1]) if not math.isnan(s200.iloc[-1]) else None,
        "sma200": _clean(round(float(s200.iloc[-1]), 2)),
        "metrics": {k: _clean(round(v, 4) if isinstance(v, float) else v) for k, v in mdl.result_dict(res).items()},
        "backtest": [{k: _clean(round(v, 4) if isinstance(v, float) else v) for k, v in s.__dict__.items()} for s in stats],
        "series": {
            "date": [str(d.date()) for d in tail.index],
            "close": [round(float(v), 2) for v in tail["Close"]],
            "sma50": [_clean(round(float(v), 2)) for v in s50],
            "sma200": [_clean(round(float(v), 2)) for v in s200],
            "p_up": [_clean(round(float(v), 3)) for v in pr],
        },
    }


def _job(args):
    import os

    os.environ.setdefault("OMP_NUM_THREADS", "2")  # workers must not each grab every core
    symbol, horizon, kind, step = args
    t0 = time.time()
    try:
        d = compute_symbol(symbol, horizon, kind, step)
        d["seconds"] = round(time.time() - t0, 1)
        return d
    except Exception as e:  # noqa: BLE001 - one bad symbol must not kill the site build
        return {"symbol": display_name(to_yahoo(symbol)), "error": str(e)}


def build(symbols: list[str] | None = None, horizon: int = 5, kind: str = "gbm", step: int = 126, workers: int = 2) -> list[dict]:
    symbols = symbols or DEFAULT_SYMBOLS
    APP_DATA.mkdir(parents=True, exist_ok=True)
    # Warm the shared caches once so worker processes only read CSVs.
    fetch_context()
    for s in symbols:
        try:
            fetch(s)
        except Exception:  # noqa: BLE001
            pass

    jobs = [(s, horizon, kind, step) for s in symbols]
    with ProcessPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(_job, jobs))

    errors = {}
    for d in results:
        if "error" in d:
            errors[d["symbol"]] = d["error"]
            continue
        (APP_DATA / f"{d['symbol']}.json").write_text(json.dumps(d, separators=(",", ":")), encoding="utf-8")

    # Index is rebuilt from every symbol file on disk, so a partial run never drops the others.
    index = []
    for p in sorted(APP_DATA.glob("*.json")):
        if p.name == "index.json":
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        index.append({
            "symbol": d["symbol"], "close": d["close"], "last_date": d["last_date"], "p_up": d["p_up"],
            "auc": d["metrics"]["auc"], "accuracy": d["metrics"]["accuracy"],
            "baseline": d["metrics"]["baseline_always_up"], "above_sma200": d["above_sma200"],
        })
    index += [{"symbol": s, "error": e} for s, e in errors.items()]
    index.sort(key=lambda r: -(r.get("p_up") or 0))
    (APP_DATA / "index.json").write_text(
        json.dumps({"generated": pd.Timestamp.utcnow().strftime("%Y-%m-%d %H:%M UTC"), "horizon": horizon,
                    "model": kind, "symbols": index}, separators=(",", ":")), encoding="utf-8")
    return results
