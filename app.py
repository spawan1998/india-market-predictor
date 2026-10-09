"""Streamlit front end for india-market-predictor.

Run locally:   streamlit run app.py
Host for free: share.streamlit.io -> New app -> this repo -> main file app.py
"""
from __future__ import annotations

import datetime as dt
import tempfile
from pathlib import Path

import pandas as pd
import streamlit as st

from market_predictor import backtest as bt
from market_predictor import model as mdl
from market_predictor.data import fetch, fetch_context
from market_predictor.report import equity_chart, price_chart
from market_predictor.scan import position_size, scan
from market_predictor.universe import NIFTY50, display_name, to_yahoo

st.set_page_config(page_title="India Market Predictor", page_icon="📈", layout="wide")
st.title("India Market Predictor")
st.caption(
    "Educational tool. The probability is only as good as the walk-forward record printed next to it. "
    "Not investment advice. Source and course: github.com/spawan1998/india-market-predictor"
)


@st.cache_data(ttl=6 * 3600, show_spinner="Downloading prices and running the walk-forward evaluation (about a minute)...")
def evaluate(symbol: str, horizon: int, kind: str, day: str):
    df = fetch(symbol)
    ctx = fetch_context()
    X, y, _ = mdl.prepare(df, ctx, horizon)
    probs, res = mdl.walk_forward(X, y, kind=kind, horizon=horizon)
    full = mdl.fit_full(X, y, kind=kind, horizon=horizon)
    p = float(full.predict_proba(X.iloc[[-1]])[:, 1][0])
    stats, curves = bt.compare(df["Close"], probs, 0.55, 0.05, 20.0)
    return df, probs, mdl.result_dict(res), p, [s.__dict__ for s in stats], curves


@st.cache_data(ttl=6 * 3600, show_spinner="Scanning NIFTY 50...")
def run_scan(day: str):
    return scan()


with st.sidebar:
    st.header("Settings")
    choice = st.selectbox("Symbol", ["NIFTY50", "BANKNIFTY", "SENSEX"] + NIFTY50, index=0)
    custom = st.text_input("or any NSE symbol / Yahoo ticker", "")
    symbol = custom.strip() or choice
    horizon = st.select_slider("Horizon (sessions)", [1, 2, 3, 5, 10, 20], value=5)
    kind = st.radio("Model", ["gbm", "logit"], horizontal=True)
    st.divider()
    capital = st.number_input("Capital (Rs)", min_value=10_000, value=200_000, step=10_000)
    risk = st.slider("Risk per trade (%)", 0.25, 2.0, 1.0, 0.25)

today = dt.date.today().isoformat()
tab_pred, tab_scan, tab_how = st.tabs(["Prediction", "NIFTY 50 scan", "How to read this"])

with tab_pred:
    try:
        df, probs, res, p, stats, curves = evaluate(symbol, horizon, kind, today)
    except Exception as e:  # noqa: BLE001
        st.error(f"Could not load {symbol}: {e}")
        st.stop()
    name = display_name(to_yahoo(symbol))
    sma200 = df["Close"].rolling(200).mean().iloc[-1]
    above = df["Close"].iloc[-1] > sma200

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(f"{name} close", f"{df['Close'].iloc[-1]:,.2f}", str(df.index[-1].date()))
    c2.metric(f"P(up in {horizon} sessions)", f"{p:.3f}", mdl.describe_probability(p))
    c3.metric("Walk-forward AUC", f"{res['auc']:.3f}", "0.50 = coin flip")
    c4.metric("200-day SMA", f"{sma200:,.0f}", "price ABOVE" if above else "price BELOW")

    if pd.isna(res["auc"]) or res["auc"] < 0.53:
        st.warning("No proven edge on this symbol: out-of-sample AUC is about 0.5, so treat the probability as noise. "
                   "Lean on the 200-day SMA regime line instead.")
    else:
        st.success("Small out-of-sample edge (AUC at or above 0.53). Still size by risk, not by conviction.")

    st.write(
        f"Out-of-sample record: accuracy {res['accuracy']:.3f}, balanced {res['balanced_accuracy']:.3f}, "
        f"always-up baseline {res['baseline_always_up']:.3f}, {res['n_predictions']} predictions, {res['n_retrains']} retrains."
    )

    tmp = Path(tempfile.gettempdir())
    st.image(str(price_chart(df, probs, name, tmp / f"{name}_price.png")))
    st.subheader("Long/flat rules vs buy-and-hold, after 20 bps per switch")
    tbl = pd.DataFrame(stats).set_index("name")[["cagr", "max_drawdown", "sharpe", "time_in_market", "n_trades", "hit_rate"]]
    st.dataframe(tbl.style.format({"cagr": "{:+.1%}", "max_drawdown": "{:+.1%}", "sharpe": "{:.2f}",
                                   "time_in_market": "{:.0%}", "hit_rate": "{:.1%}"}))
    st.image(str(equity_chart(curves, name, tmp / f"{name}_equity.png")))

with tab_scan:
    sc = run_scan(today)
    st.write(f"NIFTY 3-month return: {sc.attrs.get('nifty_ret_3m', float('nan')):+.1%}. "
             "Score 0-5 sums trend, relative momentum, breakout proximity, RSI zone and volume.")
    show = sc[["symbol", "close", "score", "rsi14", "ret_1m", "rel_3m", "vs_sma50", "vs_sma200", "from_20d_high", "atr_pct"]]
    st.dataframe(show.style.format({"close": "{:,.1f}", "score": "{:.1f}", "rsi14": "{:.0f}", "ret_1m": "{:+.1%}",
                                    "rel_3m": "{:+.1%}", "vs_sma50": "{:+.1%}", "vs_sma200": "{:+.1%}",
                                    "from_20d_high": "{:+.1%}", "atr_pct": "{:.1%}"}), height=600)
    st.subheader(f"Position size for the top 5 (capital Rs {capital:,.0f}, risk {risk}% per trade, stop 2 ATR)")
    rows = [dict(symbol=r.symbol, **position_size(r.close, r.atr, capital, risk)) for _, r in sc.head(5).iterrows()]
    st.dataframe(pd.DataFrame(rows).set_index("symbol"))
    if sc.attrs.get("missing"):
        st.caption("No data for: " + ", ".join(sc.attrs["missing"]))

with tab_how:
    st.markdown((Path(__file__).parent / "docs" / "09-how-the-predictor-works.md").read_text(encoding="utf-8"))
