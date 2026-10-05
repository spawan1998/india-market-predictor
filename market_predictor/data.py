"""Price download with a simple on-disk CSV cache.

Yahoo Finance is free and good enough for daily bars. It is *not* tick-accurate
and NIFTY index volume is unreliable (often 0), so volume features are only
trusted for stocks.
"""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import pandas as pd
import yfinance as yf

from .universe import CONTEXT, to_yahoo

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "cache"
DEFAULT_START = "2008-01-01"
COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def _cache_path(ticker: str) -> Path:
    safe = ticker.replace("^", "_").replace("=", "_").replace("&", "_")
    return CACHE_DIR / f"{safe}.csv"


def _flatten(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):
        df = df.copy()
        df.columns = df.columns.get_level_values(0)
    df = df[[c for c in COLUMNS if c in df.columns]].copy()
    df.index = pd.to_datetime(df.index).tz_localize(None).normalize()
    df.index.name = "Date"
    return df.dropna(subset=["Close"])


def _is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    mtime = dt.datetime.fromtimestamp(path.stat().st_mtime)
    now = dt.datetime.now()
    # Cache written after today's 16:00 IST close is good until tomorrow;
    # anything written today after 16:00 local is treated as fresh.
    return mtime.date() == now.date() and (mtime.hour >= 16 or now.hour < 16)


def fetch(symbol: str, start: str = DEFAULT_START, refresh: bool = False) -> pd.DataFrame:
    """Return daily OHLCV for a symbol (plain NSE name, index name or Yahoo ticker)."""
    ticker = to_yahoo(symbol)
    path = _cache_path(ticker)
    if not refresh and _is_fresh(path):
        return pd.read_csv(path, index_col="Date", parse_dates=True)

    raw = yf.download(ticker, start=start, progress=False, auto_adjust=True, threads=False)
    if raw is None or raw.empty:
        if path.exists():
            return pd.read_csv(path, index_col="Date", parse_dates=True)
        raise RuntimeError(f"No data returned for {ticker}")
    df = _flatten(raw)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(path)
    return df


def fetch_many(symbols: list[str], start: str = "2022-01-01", refresh: bool = False) -> dict[str, pd.DataFrame]:
    """Download several symbols in one Yahoo call; skip ones that fail."""
    tickers = [to_yahoo(s) for s in symbols]
    out: dict[str, pd.DataFrame] = {}
    need = []
    for t in tickers:
        p = _cache_path(t)
        if not refresh and _is_fresh(p):
            out[t] = pd.read_csv(p, index_col="Date", parse_dates=True)
        else:
            need.append(t)
    if need:
        raw = yf.download(need, start=start, progress=False, auto_adjust=True, group_by="ticker", threads=True)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        for t in need:
            try:
                sub = raw[t] if len(need) > 1 else raw
                df = _flatten(sub)
                if df.empty:
                    continue
                df.to_csv(_cache_path(t))
                out[t] = df
            except (KeyError, ValueError):
                continue
    return out


def fetch_context(start: str = DEFAULT_START, refresh: bool = False) -> dict[str, pd.DataFrame]:
    """Market-context series (VIX, S&P 500, USD/INR, crude). Missing ones are skipped."""
    out = {}
    for name, ticker in CONTEXT.items():
        try:
            out[name] = fetch(ticker, start=start, refresh=refresh)
        except Exception:  # noqa: BLE001 - context is optional
            continue
    return out
