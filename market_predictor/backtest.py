"""Backtest long/flat rules on the index, with costs, against buy-and-hold.

Three signals are compared so you can see what actually earns its keep:

* ``ml``     - long when model P(up) crosses above ``threshold``; exit when it
               falls below ``threshold - hysteresis`` (hysteresis cuts churn).
* ``sma200`` - the classic trend filter: long when close > 200-day SMA.
* ``combo``  - long only when both agree.

Positions are decided at today's close and earn tomorrow's return (no
look-ahead). Each switch pays ``cost_bps`` (delivery STT 0.1% + brokerage +
slippage is realistically 15-25 bps per side).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class Stats:
    name: str
    total_return: float
    cagr: float
    sharpe: float
    max_drawdown: float
    time_in_market: float
    n_trades: int
    hit_rate: float


def _cagr(equity: pd.Series) -> float:
    years = (equity.index[-1] - equity.index[0]).days / 365.25
    return float(equity.iloc[-1] ** (1 / years) - 1) if years > 0 else float("nan")


def _sharpe(daily: pd.Series) -> float:
    sd = daily.std()
    return float(np.sqrt(252) * daily.mean() / sd) if sd > 0 else float("nan")


def _max_dd(equity: pd.Series) -> float:
    return float((equity / equity.cummax() - 1).min())


def ml_signal(probs: pd.Series, threshold: float = 0.55, hysteresis: float = 0.05) -> pd.Series:
    """Enter above ``threshold``, exit below ``threshold - hysteresis``."""
    lo = threshold - hysteresis
    pos = np.zeros(len(probs), dtype=int)
    state = 0
    for i, p in enumerate(probs.values):
        if np.isnan(p):
            pos[i] = state
            continue
        if state == 0 and p > threshold:
            state = 1
        elif state == 1 and p < lo:
            state = 0
        pos[i] = state
    return pd.Series(pos, index=probs.index)


def sma_signal(close: pd.Series, n: int = 200) -> pd.Series:
    return (close > close.rolling(n).mean()).astype(int)


def evaluate(close: pd.Series, position: pd.Series, name: str, cost_bps: float = 20.0):
    ret = close.pct_change()
    idx = position.dropna().index.intersection(ret.index)
    ret, position = ret.loc[idx], position.loc[idx].astype(int)

    held = position.shift(1).fillna(0)
    switches = position.diff().abs().fillna(position.iloc[0])
    strat = held * ret - switches * cost_bps / 10_000
    equity = (1 + strat.fillna(0)).cumprod()
    in_mkt = held == 1
    stats = Stats(
        name=name, total_return=float(equity.iloc[-1] - 1), cagr=_cagr(equity), sharpe=_sharpe(strat),
        max_drawdown=_max_dd(equity), time_in_market=float(held.mean()), n_trades=int(switches.sum()),
        hit_rate=float((ret[in_mkt] > 0).mean()) if in_mkt.any() else float("nan"),
    )
    return stats, equity


def compare(close: pd.Series, probs: pd.Series, threshold: float = 0.55, hysteresis: float = 0.05,
            cost_bps: float = 20.0) -> tuple[list[Stats], pd.DataFrame]:
    """Run ml / sma200 / combo / buy-and-hold over the out-of-sample window."""
    oos = probs.dropna().index
    close = close.loc[close.index >= oos[0]]
    p = probs.reindex(close.index)

    ml = ml_signal(p, threshold, hysteresis)
    sma = sma_signal(close.reindex(probs.index).ffill(), 200).reindex(close.index).fillna(0).astype(int)
    combo = (ml & sma).astype(int)
    bh = pd.Series(1, index=close.index)

    results, curves = [], {}
    for name, sig in (("ml", ml), ("sma200", sma), ("combo", combo), ("buy_and_hold", bh)):
        st, eq = evaluate(close, sig, name, cost_bps if name != "buy_and_hold" else 0.0)
        results.append(st)
        curves[name] = eq
    curves["ml_position"] = ml.shift(1).fillna(0)
    return results, pd.DataFrame(curves)


def threshold_sweep(close: pd.Series, probs: pd.Series, cost_bps: float = 20.0, hysteresis: float = 0.05) -> pd.DataFrame:
    rows = []
    oos = probs.dropna().index
    c = close.loc[close.index >= oos[0]]
    for thr in (0.50, 0.52, 0.55, 0.58, 0.60, 0.65):
        st, _ = evaluate(c, ml_signal(probs.reindex(c.index), thr, hysteresis), f"thr{thr}", cost_bps)
        rows.append({"threshold": thr, "cagr": st.cagr, "sharpe": st.sharpe, "max_dd": st.max_drawdown,
                     "trades": st.n_trades, "time_in_mkt": st.time_in_market})
    return pd.DataFrame(rows)
