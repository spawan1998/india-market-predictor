"""Technical indicators and the feature matrix.

Every feature is computed only from information available at the close of day
``t``; the target looks ``horizon`` days *forward*. Keeping that boundary clean
is the whole game; leaking even one future bar makes a model look brilliant in
backtests and useless live.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------- indicators ----------

def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    """Wilder's RSI, 0-100. >70 overbought, <30 oversold (in ranges, not trends)."""
    delta = close.diff()
    up = delta.clip(lower=0)
    down = -delta.clip(upper=0)
    avg_up = up.ewm(alpha=1 / n, adjust=False).mean()
    avg_down = down.ewm(alpha=1 / n, adjust=False).mean()
    rs = avg_up / avg_down.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).fillna(50)


def macd(close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    line = ema(close, fast) - ema(close, slow)
    sig = ema(line, signal)
    return line, sig, line - sig


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    """Average True Range: the day's typical movement, used for stops and sizing."""
    prev_close = df["Close"].shift(1)
    tr = pd.concat(
        [df["High"] - df["Low"], (df["High"] - prev_close).abs(), (df["Low"] - prev_close).abs()],
        axis=1,
    ).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def bollinger(close: pd.Series, n: int = 20, k: float = 2.0):
    mid = sma(close, n)
    sd = close.rolling(n).std()
    upper, lower = mid + k * sd, mid - k * sd
    pct_b = (close - lower) / (upper - lower).replace(0, np.nan)
    bandwidth = (upper - lower) / mid
    return pct_b, bandwidth


# ---------- feature matrix ----------

def _align_context(index: pd.DatetimeIndex, series: pd.Series, lag_for_overnight: bool) -> pd.Series:
    """Align a context series onto the Indian trading calendar.

    US markets close after India does, so for Indian date t the latest *known*
    S&P move is the US session dated t-1. We shift by one US session then
    forward-fill onto the Indian index.
    """
    s = series.shift(1) if lag_for_overnight else series
    return s.reindex(s.index.union(index)).ffill().reindex(index)


def build_features(df: pd.DataFrame, context: dict[str, pd.DataFrame] | None = None) -> pd.DataFrame:
    c, h, l, o, v = df["Close"], df["High"], df["Low"], df["Open"], df["Volume"]
    f = pd.DataFrame(index=df.index)

    ret = c.pct_change()
    for n in (1, 2, 3, 5, 10, 20):
        f[f"ret_{n}"] = c.pct_change(n)
    f["gap"] = o / c.shift(1) - 1
    f["range"] = (h - l) / c
    f["close_pos"] = (c - l) / (h - l).replace(0, np.nan)  # where in the day's range we closed

    for n in (10, 20, 50, 200):
        f[f"sma{n}_dist"] = c / sma(c, n) - 1
    f["sma20_50"] = sma(c, 20) / sma(c, 50) - 1
    f["sma50_200"] = sma(c, 50) / sma(c, 200) - 1
    f["ema20_slope"] = ema(c, 20).pct_change(5)

    f["rsi14"] = rsi(c, 14)
    f["rsi7"] = rsi(c, 7)
    line, sig, hist = macd(c)
    f["macd"] = line / c
    f["macd_hist"] = hist / c
    f["macd_cross"] = np.sign(hist) - np.sign(hist.shift(1))

    f["atr_pct"] = atr(df) / c
    f["vol_10"] = ret.rolling(10).std()
    f["vol_20"] = ret.rolling(20).std()
    f["vol_ratio"] = f["vol_10"] / f["vol_20"]

    pct_b, bw = bollinger(c)
    f["bb_pct"] = pct_b
    f["bb_width"] = bw

    f["hi20_dist"] = c / h.rolling(20).max() - 1
    f["lo20_dist"] = c / l.rolling(20).min() - 1
    f["hi52_dist"] = c / h.rolling(252).max() - 1

    if v.replace(0, np.nan).notna().mean() > 0.8:  # volume is usable (stocks, not indices)
        lv = np.log1p(v.replace(0, np.nan))
        f["vol_z20"] = (lv - lv.rolling(20).mean()) / lv.rolling(20).std()
        f["vol_trend"] = v.rolling(5).mean() / v.rolling(20).mean() - 1

    f["dow"] = df.index.dayofweek
    f["month_end"] = (df.index.to_period("M") != df.index.shift(1, freq="B").to_period("M")).astype(int)

    if context:
        if "vix" in context:
            vix = context["vix"]["Close"]
            f["vix"] = _align_context(df.index, vix, False)
            f["vix_chg5"] = _align_context(df.index, vix.pct_change(5), False)
        if "spx" in context:
            spx = context["spx"]["Close"]
            f["spx_ret1"] = _align_context(df.index, spx.pct_change(), True)
            f["spx_ret5"] = _align_context(df.index, spx.pct_change(5), True)
            f["spx_sma50"] = _align_context(df.index, spx / sma(spx, 50) - 1, True)
        if "usdinr" in context:
            inr = context["usdinr"]["Close"]
            f["inr_ret5"] = _align_context(df.index, inr.pct_change(5), False)
        if "crude" in context:
            cr = context["crude"]["Close"]
            f["crude_ret5"] = _align_context(df.index, cr.pct_change(5), True)

    return f.replace([np.inf, -np.inf], np.nan)


def build_target(df: pd.DataFrame, horizon: int = 5) -> tuple[pd.Series, pd.Series]:
    """Forward return over ``horizon`` sessions and its direction (1 = up)."""
    fwd = df["Close"].shift(-horizon) / df["Close"] - 1
    return fwd, (fwd > 0).astype(int).where(fwd.notna())
