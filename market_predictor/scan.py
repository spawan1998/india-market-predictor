"""NIFTY 50 swing-trade scanner.

This is *not* the ML model. It is a rules-based screen that ranks stocks by
trend + momentum and tells you what a risk-controlled position would look like.
Use it to build a short watchlist, then do your own chart check.

Score components (each 0-1, summed):
  trend     : close > SMA50 > SMA200 (stacked moving averages)
  momentum  : 3-month return relative to NIFTY (relative strength)
  breakout  : closeness to 20-day high
  rsi_ok    : RSI between 45 and 70 (strong but not stretched)
  volume    : 5-day avg volume above 20-day avg (participation)
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

from .data import fetch, fetch_many
from .features import atr, rsi, sma
from .universe import NIFTY50, display_name


def _row(ticker: str, df: pd.DataFrame, nifty_ret63: float) -> dict | None:
    if len(df) < 220:
        return None
    c = df["Close"]
    last = float(c.iloc[-1])
    s50, s200 = float(sma(c, 50).iloc[-1]), float(sma(c, 200).iloc[-1])
    r14 = float(rsi(c).iloc[-1])
    a14 = float(atr(df).iloc[-1])
    ret21 = float(c.iloc[-1] / c.iloc[-22] - 1)
    ret63 = float(c.iloc[-1] / c.iloc[-64] - 1)
    hi20 = float(df["High"].rolling(20).max().iloc[-1])
    vol5 = float(df["Volume"].iloc[-5:].mean())
    vol20 = float(df["Volume"].iloc[-20:].mean())

    trend = 1.0 if last > s50 > s200 else (0.5 if last > s200 else 0.0)
    rel = ret63 - nifty_ret63
    momentum = float(np.clip((rel + 0.05) / 0.20, 0, 1))
    breakout = float(np.clip(1 - (hi20 - last) / hi20 / 0.05, 0, 1))
    rsi_ok = 1.0 if 45 <= r14 <= 70 else (0.3 if 40 <= r14 <= 75 else 0.0)
    volume = 1.0 if vol20 > 0 and vol5 > vol20 else 0.0
    score = trend + momentum + breakout + rsi_ok + volume

    return {
        "symbol": display_name(ticker), "close": last, "rsi14": r14,
        "ret_1m": ret21, "ret_3m": ret63, "rel_3m": rel,
        "vs_sma50": last / s50 - 1, "vs_sma200": last / s200 - 1,
        "from_20d_high": last / hi20 - 1, "atr_pct": a14 / last, "atr": a14,
        "score": score,
    }


def scan(symbols: list[str] | None = None, refresh: bool = False) -> pd.DataFrame:
    symbols = symbols or NIFTY50
    nifty = fetch("NIFTY50", refresh=refresh)
    nifty_ret63 = float(nifty["Close"].iloc[-1] / nifty["Close"].iloc[-64] - 1)
    data = fetch_many(symbols, start="2023-01-01", refresh=refresh)
    rows = [r for t, df in data.items() if (r := _row(t, df, nifty_ret63))]
    out = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
    out.attrs["nifty_ret_3m"] = nifty_ret63
    out.attrs["missing"] = sorted(set(symbols) - {display_name(t) for t in data})
    return out


def position_size(entry: float, atr_value: float, capital: float, risk_pct: float = 1.0,
                  atr_mult: float = 2.0) -> dict:
    """Shares to buy so that a stop ``atr_mult`` ATRs below entry loses ``risk_pct`` of capital.

    This is the single most important formula in the repo. Risk per trade is
    chosen first; position size falls out of it, never the other way round.
    """
    stop = entry - atr_mult * atr_value
    risk_per_share = entry - stop
    rupees_at_risk = capital * risk_pct / 100
    qty = math.floor(rupees_at_risk / risk_per_share) if risk_per_share > 0 else 0
    # Never let one position exceed 25% of capital, regardless of how tight the stop is.
    qty = min(qty, math.floor(0.25 * capital / entry))
    return {
        "entry": entry, "stop": round(stop, 2), "target_2R": round(entry + 2 * risk_per_share, 2),
        "qty": qty, "position_value": round(qty * entry, 2),
        "rupees_at_risk": round(qty * risk_per_share, 2),
    }
