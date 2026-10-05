import numpy as np
import pandas as pd

from market_predictor.features import atr, build_features, build_target, rsi
from market_predictor.scan import position_size


def _fake_ohlcv(n=400, seed=0):
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2020-01-01", periods=n)
    close = 100 * np.cumprod(1 + rng.normal(0, 0.01, n))
    high = close * (1 + rng.uniform(0, 0.01, n))
    low = close * (1 - rng.uniform(0, 0.01, n))
    open_ = low + (high - low) * rng.uniform(0, 1, n)
    vol = rng.integers(1_000_000, 5_000_000, n)
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": vol}, index=idx)


def test_rsi_bounds():
    df = _fake_ohlcv()
    r = rsi(df["Close"])
    assert r.between(0, 100).all()


def test_atr_positive():
    df = _fake_ohlcv()
    assert (atr(df).dropna() > 0).all()


def test_features_do_not_use_future():
    """Truncating the data must not change earlier feature rows."""
    df = _fake_ohlcv()
    full = build_features(df)
    cut = build_features(df.iloc[:-30])
    common = cut.index
    pd.testing.assert_frame_equal(full.loc[common], cut, check_exact=False, atol=1e-9)


def test_target_alignment():
    df = _fake_ohlcv()
    fwd, y = build_target(df, horizon=5)
    assert fwd.iloc[-5:].isna().all()
    expected = df["Close"].iloc[5] / df["Close"].iloc[0] - 1
    assert abs(fwd.iloc[0] - expected) < 1e-12
    assert set(y.dropna().unique()) <= {0, 1}


def test_position_size_respects_risk_and_cap():
    s = position_size(entry=1000, atr_value=20, capital=200_000, risk_pct=1.0)
    assert s["stop"] == 960
    assert s["rupees_at_risk"] <= 2000
    assert s["position_value"] <= 50_000  # 25% cap
    tight = position_size(entry=1000, atr_value=0.5, capital=200_000, risk_pct=1.0)
    assert tight["position_value"] <= 50_000
