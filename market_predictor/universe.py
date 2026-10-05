"""Ticker universe and Yahoo Finance symbol helpers.

NSE stocks on Yahoo Finance carry the ``.NS`` suffix (``RELIANCE.NS``); BSE uses
``.BO``. Indices use caret symbols (``^NSEI`` = NIFTY 50, ``^NSEBANK`` = BANK NIFTY).

The NIFTY 50 list is rebalanced twice a year (March and September). Update
``NIFTY50`` when constituents change; the scanner tolerates symbols that fail.
"""

INDICES = {
    "NIFTY50": "^NSEI",
    "BANKNIFTY": "^NSEBANK",
    "SENSEX": "^BSESN",
    "INDIAVIX": "^INDIAVIX",
}

# Market context series used as features for the index model.
CONTEXT = {
    "vix": "^INDIAVIX",   # India VIX: implied volatility of NIFTY options
    "spx": "^GSPC",       # S&P 500: overnight global cue
    "usdinr": "USDINR=X",  # Rupee; weak rupee -> FII outflow pressure
    "crude": "CL=F",      # WTI crude: India is a big importer
}

# NIFTY 50 constituents (as known in late 2025; verify against nseindia.com).
NIFTY50 = [
    "ADANIENT", "ADANIPORTS", "APOLLOHOSP", "ASIANPAINT", "AXISBANK",
    "BAJAJ-AUTO", "BAJFINANCE", "BAJAJFINSV", "BEL", "BHARTIARTL",
    "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT", "ETERNAL",
    "GRASIM", "HCLTECH", "HDFCBANK", "HDFCLIFE", "HINDALCO",
    "HINDUNILVR", "ICICIBANK", "INDIGO", "INFY", "ITC",
    "JIOFIN", "JSWSTEEL", "KOTAKBANK", "LT", "M&M",
    "MARUTI", "MAXHEALTH", "NESTLEIND", "NTPC", "ONGC",
    "POWERGRID", "RELIANCE", "SBILIFE", "SBIN", "SHRIRAMFIN",
    "SUNPHARMA", "TCS", "TATACONSUM", "TMPV", "TMCV", "TATASTEEL",
    "TECHM", "TITAN", "TRENT", "ULTRACEMCO", "WIPRO",
]
# TMPV / TMCV = Tata Motors passenger / commercial vehicles after the Oct 2025
# demerger (the old TATAMOTORS symbol no longer resolves on Yahoo).


def to_yahoo(symbol: str) -> str:
    """Map a plain NSE symbol or index name to a Yahoo Finance ticker."""
    s = symbol.strip().upper()
    if s in INDICES:
        return INDICES[s]
    if s.startswith("^") or s.endswith((".NS", ".BO")) or "=" in s:
        return s
    return f"{s}.NS"


def display_name(ticker: str) -> str:
    for name, yt in INDICES.items():
        if yt == ticker:
            return name
    return ticker.replace(".NS", "")
