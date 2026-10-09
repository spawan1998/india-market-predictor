"""Paper-trading challenge: a rules-based swing trader with written reasoning.

Runs once per trading day after the close (the daily GitHub Action does it).
State lives in ``paper/state.json``; every decision and the reason for it is
appended to ``paper/journal.md`` so a beginner can follow along.

The rules are the course's rules (docs/02, 04, 06):

Entry (orders placed at the close, filled at the next session's open):
  * stock in a stacked uptrend: close > SMA 50 > SMA 200
  * relative strength: beat NIFTY over the last 3 months
  * RSI 14 between 45 and 70 (strong, not stretched)
  * within 3% of its 20-day high (breakout / near breakout)
  * at most 4 open positions, at most 2 new entries per day
  * if NIFTY itself is below its 200-day SMA, risk is halved (0.5% instead of 1%)
Sizing: risk% of equity, stop 2 ATR below entry, position capped at 25% of equity.
Exits (checked on each day's high/low):
  * stop hit -> out at the stop (or at the open if it gapped through)
  * +2R target hit -> sell half, move stop to breakeven, trail the rest 2 ATR below the highest close
  * 10 sessions held and still below entry -> out at the close ("it is not working")
  * last session of the challenge -> everything closed at the close
Costs: 0.2% per side (STT, brokerage, slippage).
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from .data import fetch, fetch_many
from .features import atr, sma
from .scan import position_size, scan
from .universe import NIFTY50, to_yahoo

PAPER_DIR = Path(__file__).resolve().parent.parent / "paper"
STATE = PAPER_DIR / "state.json"
JOURNAL = PAPER_DIR / "journal.md"
APP_INDEX = Path(__file__).resolve().parent.parent / "app" / "data" / "index.json"

COST = 0.002          # per side
MAX_POS = 4
MAX_NEW_PER_DAY = 2
TIME_STOP = 10        # sessions
ATR_MULT = 2.0


def _load() -> dict | None:
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else None


def _save(s: dict):
    PAPER_DIR.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(s, indent=1), encoding="utf-8")


def _rs(x: float) -> str:
    return f"Rs {x:,.0f}"


def init(capital: float, sessions: int = 15) -> dict:
    s = {
        "capital_start": capital, "cash": capital, "max_sessions": sessions, "sessions_done": 0,
        "created": dt.date.today().isoformat(), "last_run_date": None, "finished": False,
        "positions": [], "pending": [], "closed": [], "equity": [],
    }
    _save(s)
    JOURNAL.write_text(
        f"# Paper-trading challenge\n\nVirtual capital {_rs(capital)}, {sessions} trading sessions, "
        f"NSE cash delivery only, rules from the course (entry: stacked uptrend + beating NIFTY + RSI 45-70 + near 20-day high; "
        f"stop 2 ATR; half off at +2R then trail; time stop 10 sessions; max 4 positions; 0.2% cost per side). "
        f"Created {s['created']}. Every entry and exit below carries its reason. "
        f"Orders are decided at the close and filled at the next session's open.\n", encoding="utf-8")
    return s


def _p_up() -> dict[str, float]:
    if not APP_INDEX.exists():
        return {}
    d = json.loads(APP_INDEX.read_text(encoding="utf-8"))
    return {r["symbol"]: r.get("p_up") for r in d["symbols"] if "p_up" in r}


def run(refresh: bool = True) -> str:
    s = _load()
    if s is None:
        raise RuntimeError("no paper state; run `imp paper --init --capital 200000` first")
    if s["finished"]:
        return "challenge already finished; see paper/journal.md"

    nifty = fetch("NIFTY50", refresh=refresh)
    data = fetch_many(NIFTY50, start="2023-01-01", refresh=refresh)
    day = nifty.index[-1]
    if s["last_run_date"] == str(day.date()):
        return f"already processed {day.date()}"
    sc = scan(refresh=False)
    pup = _p_up()
    n_close = float(nifty["Close"].iloc[-1])
    n_sma200 = float(sma(nifty["Close"], 200).iloc[-1])
    bull = n_close > n_sma200
    session_no = s["sessions_done"] + 1
    last_session = session_no >= s["max_sessions"]
    lines = [f"\n## Session {session_no} of {s['max_sessions']}: {day.date()}\n",
             f"NIFTY {n_close:,.0f}, {'ABOVE' if bull else 'BELOW'} its 200-day SMA ({n_sma200:,.0f}): "
             + ("normal risk, 1% of equity per trade." if bull else
                "defensive mode, risk halved to 0.5% of equity per trade, because the index trend is against new longs.")]

    def bar(sym: str):
        df = data.get(to_yahoo(sym))
        if df is None or df.index[-1] != day:
            return None
        return df.iloc[-1], df

    def mark_to_market() -> float:
        return s["cash"] + sum(p["qty"] * float(bar(p["symbol"])[0]["Close"]) for p in s["positions"] if bar(p["symbol"]))

    # ---- 1. fill yesterday's orders at today's open ----
    for o in s["pending"]:
        b = bar(o["symbol"])
        if b is None:
            lines.append(f"- Order for {o['symbol']} not filled: no price bar for {day.date()}. Dropped.")
            continue
        row, df = b
        entry = float(row["Open"])
        a = float(atr(df).iloc[-2])  # ATR known when the order was placed (yesterday's close)
        sz = position_size(entry, a, mark_to_market(), o["risk_pct"], ATR_MULT)
        if sz["qty"] < 1 or sz["qty"] * entry * (1 + COST) > s["cash"]:
            lines.append(f"- Order for {o['symbol']} skipped: {sz['qty']} shares at {entry:,.2f} do not fit the cash left ({_rs(s['cash'])}).")
            continue
        cost = sz["qty"] * entry * COST
        s["cash"] -= sz["qty"] * entry + cost
        s["positions"].append({
            "symbol": o["symbol"], "qty": sz["qty"], "entry": entry, "entry_date": str(day.date()),
            "stop": sz["stop"], "target": sz["target_2R"], "r": entry - sz["stop"], "atr": a,
            "half_taken": False, "highest_close": entry, "sessions": 0, "reason": o["reason"]})
        lines.append(f"- **ENTERED {o['symbol']}**: {sz['qty']} shares at the open {entry:,.2f} (cost {_rs(cost)}). "
                     f"Stop {sz['stop']:,.2f} (2 ATR below, risking {_rs(sz['rupees_at_risk'])} = 1R), first target {sz['target_2R']:,.2f} (+2R). "
                     f"Why: {o['reason']}")
    s["pending"] = []

    # ---- 2. manage open positions on today's bar ----
    still = []
    for p in s["positions"]:
        b = bar(p["symbol"])
        if b is None:
            still.append(p)
            continue
        row, df = b
        o, h, l, c = (float(row[k]) for k in ("Open", "High", "Low", "Close"))
        entered_today = p["entry_date"] == str(day.date())
        if not entered_today:
            p["sessions"] += 1
        exit_px, why = None, None
        if o <= p["stop"] and not entered_today:
            exit_px, why = o, f"gapped below the stop {p['stop']:,.2f} at the open; the plan says exit at the open, no waiting"
        elif l <= p["stop"]:
            exit_px, why = p["stop"], f"stop {p['stop']:,.2f} was hit (day's low {l:,.2f}); a stop is not negotiable"
        elif not p["half_taken"] and h >= p["target"]:
            half = max(1, p["qty"] // 2) if p["qty"] > 1 else p["qty"]
            px = p["target"]
            s["cash"] += half * px * (1 - COST)
            pnl = half * (px - p["entry"]) - half * (px + p["entry"]) * COST
            s["closed"].append({"symbol": p["symbol"], "qty": half, "entry": p["entry"], "exit": px, "entry_date": p["entry_date"],
                                "exit_date": str(day.date()), "pnl": round(pnl, 2), "r_multiple": round((px - p["entry"]) / p["r"], 2),
                                "why": "first target +2R hit: booked half, stop to breakeven, trailing the rest"})
            p["qty"] -= half
            p["half_taken"] = True
            p["stop"] = p["entry"]
            lines.append(f"- **{p['symbol']} hit the +2R target {px:,.2f}**: sold {half} shares there ({_rs(pnl)} profit). "
                         f"Stop on the remaining {p['qty']} moved to breakeven {p['entry']:,.2f}; from here it trails 2 ATR under the highest close.")
            if p["qty"] == 0:
                continue
        if exit_px is None and p["sessions"] >= TIME_STOP and c < p["entry"]:
            exit_px, why = c, f"held {p['sessions']} sessions and still below entry; time stop, the idea is not working"
        if exit_px is None and last_session:
            exit_px, why = c, "last session of the challenge, all positions closed at the close"
        if exit_px is not None:
            s["cash"] += p["qty"] * exit_px * (1 - COST)
            pnl = p["qty"] * (exit_px - p["entry"]) - p["qty"] * (exit_px + p["entry"]) * COST
            rm = (exit_px - p["entry"]) / p["r"]
            s["closed"].append({"symbol": p["symbol"], "qty": p["qty"], "entry": p["entry"], "exit": exit_px, "entry_date": p["entry_date"],
                                "exit_date": str(day.date()), "pnl": round(pnl, 2), "r_multiple": round(rm, 2), "why": why})
            lines.append(f"- **EXITED {p['symbol']}**: {p['qty']} shares at {exit_px:,.2f}, P&L {_rs(pnl)} ({rm:+.1f}R). Why: {why}.")
            continue
        p["highest_close"] = max(p["highest_close"], c)
        if p["half_taken"]:
            new_stop = round(p["highest_close"] - ATR_MULT * float(atr(df).iloc[-1]), 2)
            if new_stop > p["stop"]:
                lines.append(f"- {p['symbol']}: trailing stop raised {p['stop']:,.2f} -> {new_stop:,.2f} (2 ATR under the highest close {p['highest_close']:,.2f}).")
                p["stop"] = new_stop
        unreal = p["qty"] * (c - p["entry"])
        lines.append(f"- Holding {p['symbol']}: {p['qty']} shares, close {c:,.2f}, {unreal:+,.0f} unrealised ({(c - p['entry']) / p['r']:+.1f}R), stop {p['stop']:,.2f}, target {p['target']:,.2f}.")
        still.append(p)
    s["positions"] = still

    # ---- 3. new orders for tomorrow's open ----
    if session_no < s["max_sessions"] - 1:
        slots = MAX_POS - len(s["positions"])
        held = {p["symbol"] for p in s["positions"]}
        cands = []
        for r in sc.itertuples():
            if r.symbol in held:
                continue
            stacked = r.vs_sma50 > 0 and r.vs_sma200 > 0 and r.vs_sma50 < r.vs_sma200  # close > SMA50 > SMA200
            if stacked and r.rel_3m > 0 and 45 <= r.rsi14 <= 70 and r.from_20d_high >= -0.03 and r.atr_pct >= 0.01:
                cands.append(r)
        cands.sort(key=lambda r: (r.score, pup.get(r.symbol) or 0.5), reverse=True)
        risk = 1.0 if bull else 0.5
        picked = cands[:max(0, min(slots, MAX_NEW_PER_DAY))]
        if slots <= 0:
            lines.append("- No new orders: already holding the maximum of 4 positions.")
        elif not cands:
            lines.append("- No new orders: no NIFTY 50 stock passed all entry rules today (close above SMA 50 above SMA 200, "
                         "beating NIFTY over 3 months, RSI 45-70, within 3% of its 20-day high). Cash is a position.")
        for r in picked:
            pu = pup.get(r.symbol)
            reason = (f"close {r.close:,.2f} is above its 50-day and 200-day averages ({r.vs_sma50:+.1%} / {r.vs_sma200:+.1%}), "
                      f"it beat NIFTY by {r.rel_3m:+.1%} over 3 months, RSI {r.rsi14:.0f}, {r.from_20d_high:+.1%} from its 20-day high, "
                      f"scan score {r.score:.1f}/5" + (f", model P(up) {pu:.2f} (tie-breaker only, no proven edge)" if pu is not None else ""))
            s["pending"].append({"symbol": r.symbol, "risk_pct": risk, "reason": reason})
            lines.append(f"- **ORDER for the next open: buy {r.symbol}** (risk {risk}% of equity, stop 2 ATR = about {ATR_MULT * r.atr:,.0f} below entry). Why: {reason}.")
        rejected = cands[len(picked):][:3]
        if rejected:
            lines.append("- Also qualified but not taken (slot or daily limit): " + ", ".join(r.symbol for r in rejected) + ".")
    else:
        lines.append("- No new orders: the challenge ends too soon for a new swing trade to play out.")

    # ---- 4. mark to market ----
    equity = mark_to_market()
    if not s["equity"]:
        s["nifty_start"] = n_close
    s["equity"].append({"date": str(day.date()), "equity": round(equity, 2), "cash": round(s["cash"], 2), "nifty": n_close})
    ret = equity / s["capital_start"] - 1
    nret = n_close / s["nifty_start"] - 1
    lines.append(f"\nEquity {_rs(equity)} ({ret:+.2%} since start) vs NIFTY {nret:+.2%}. Cash {_rs(s['cash'])}, "
                 f"{len(s['positions'])} open position(s), {len(s['pending'])} order(s) for the next open.")

    s["sessions_done"] = session_no
    s["last_run_date"] = str(day.date())
    if last_session:
        s["finished"] = True
        wins = [t for t in s["closed"] if t["pnl"] > 0]
        total = sum(t["pnl"] for t in s["closed"])
        lines.append(f"\n## Final result\n\nClosed trades: {len(s['closed'])}, winners {len(wins)}, realised P&L {_rs(total)} "
                     f"({total / s['capital_start']:+.2%}) vs NIFTY {nret:+.2%} over the same {s['max_sessions']} sessions. "
                     "Fifteen sessions is far too few to judge a method; the point was to show the discipline, not the number.")
        lines.append("\n| symbol | entry date | entry | exit date | exit | qty | P&L | R | why |\n|---|---|---|---|---|---|---|---|---|")
        for t in s["closed"]:
            lines.append(f"| {t['symbol']} | {t['entry_date']} | {t['entry']:,.2f} | {t['exit_date']} | {t['exit']:,.2f} | {t['qty']} | {t['pnl']:+,.0f} | {t['r_multiple']:+.1f} | {t['why']} |")
    _save(s)
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return "\n".join(lines)


def status() -> str:
    s = _load()
    if s is None:
        return "no paper challenge running"
    e = s["equity"][-1] if s["equity"] else None
    out = [f"session {s['sessions_done']}/{s['max_sessions']}, finished={s['finished']}, cash {_rs(s['cash'])}"]
    if e:
        out.append(f"equity {_rs(e['equity'])} ({e['equity'] / s['capital_start'] - 1:+.2%}) on {e['date']}; NIFTY {e['nifty'] / s['nifty_start'] - 1:+.2%}")
    for p in s["positions"]:
        out.append(f"  open {p['symbol']} x{p['qty']} @ {p['entry']:,.2f} stop {p['stop']:,.2f} target {p['target']:,.2f}")
    for o in s["pending"]:
        out.append(f"  order {o['symbol']} for the next open (risk {o['risk_pct']}%)")
    out.append(f"  closed trades: {len(s['closed'])}, realised {_rs(sum(t['pnl'] for t in s['closed']))}")
    return "\n".join(out)
