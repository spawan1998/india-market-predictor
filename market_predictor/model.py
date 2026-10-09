"""Direction model with honest walk-forward evaluation.

We predict P(close in ``horizon`` sessions > close today). Two models:

* ``gbm``   - HistGradientBoostingClassifier (handles NaNs, captures interactions)
* ``logit`` - regularised logistic regression (linear baseline; hard to beat!)

Walk-forward: train on everything up to date T, predict the next ``step``
sessions, roll forward, repeat. Every prediction is out-of-sample. If accuracy
comes out at 52-56% that is *normal* for daily equity direction; anything above
60% on an index usually means a leak.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .features import build_features, build_target

MODEL_DIR = Path(__file__).resolve().parent.parent / "models"


def make_model(kind: str = "gbm"):
    if kind == "gbm":
        return HistGradientBoostingClassifier(
            max_iter=300, learning_rate=0.03, max_depth=3, min_samples_leaf=40,
            l2_regularization=1.0, random_state=42,
        )
    if kind == "logit":
        return Pipeline([
            ("impute", SimpleImputer(strategy="median")),
            ("scale", StandardScaler()),
            ("clf", LogisticRegression(C=0.1, max_iter=2000)),
        ])
    raise ValueError(f"unknown model kind {kind!r}")


@dataclass
class EvalResult:
    accuracy: float
    balanced_accuracy: float
    auc: float
    baseline_always_up: float
    n_predictions: int
    n_retrains: int


def prepare(df: pd.DataFrame, context: dict | None, horizon: int):
    X = build_features(df, context)
    fwd, y = build_target(df, horizon)
    # Need a 200-day SMA, so drop the warm-up period.
    valid = X.index[X["sma200_dist"].notna()]
    return X.loc[valid], y.loc[valid], fwd.loc[valid]


def walk_forward(
    X: pd.DataFrame, y: pd.Series, kind: str = "gbm",
    min_train: int = 750, step: int = 63, horizon: int = 5,
) -> tuple[pd.Series, EvalResult]:
    """Expanding-window walk-forward. Returns out-of-sample P(up) and metrics."""
    probs = pd.Series(np.nan, index=X.index)
    n = len(X)
    retrains = 0
    # Recently listed names: shrink the initial window so there is still an out-of-sample record.
    min_train = min(min_train, max(250, n // 2))
    for start in range(min_train, n, step):
        # Leave a 'horizon' gap so training labels never peek into the test block.
        train_idx = slice(0, start - horizon)
        test_idx = slice(start, min(start + step, n))
        ytr = y.iloc[train_idx]
        mask = ytr.notna()
        if mask.sum() < 200:
            continue
        model = make_model(kind)
        model.fit(X.iloc[train_idx][mask.values], ytr[mask].astype(int))
        probs.iloc[test_idx] = model.predict_proba(X.iloc[test_idx])[:, 1]
        retrains += 1

    both = pd.concat([probs, y], axis=1, keys=["p", "y"]).dropna()
    if both.empty:
        return probs, EvalResult(float("nan"), float("nan"), float("nan"), float("nan"), 0, retrains)
    pred = (both["p"] > 0.5).astype(int)
    res = EvalResult(
        accuracy=float(accuracy_score(both["y"], pred)),
        balanced_accuracy=float(balanced_accuracy_score(both["y"], pred)),
        auc=float(roc_auc_score(both["y"], both["p"])) if both["y"].nunique() > 1 else float("nan"),
        baseline_always_up=float(both["y"].mean()),
        n_predictions=int(len(both)),
        n_retrains=retrains,
    )
    return probs, res


def fit_full(X: pd.DataFrame, y: pd.Series, kind: str = "gbm", horizon: int = 5):
    """Fit on all labelled rows (the last ``horizon`` rows have no label yet)."""
    mask = y.notna()
    model = make_model(kind)
    model.fit(X[mask.values], y[mask].astype(int))
    return model


def feature_importance(model, X: pd.DataFrame, y: pd.Series, n_repeats: int = 5) -> pd.Series:
    """Permutation importance on the last 2 years (what the model actually leans on)."""
    from sklearn.inspection import permutation_importance

    mask = y.notna()
    Xs, ys = X[mask.values].iloc[-504:], y[mask].iloc[-504:].astype(int)
    r = permutation_importance(model, Xs, ys, n_repeats=n_repeats, random_state=0, scoring="roc_auc")
    return pd.Series(r.importances_mean, index=X.columns).sort_values(ascending=False)


def save(model, name: str) -> Path:
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    p = MODEL_DIR / f"{name}.joblib"
    joblib.dump(model, p)
    return p


def describe_probability(p: float) -> str:
    """Translate P(up) into a plain-English stance. Thresholds are deliberately wide."""
    if p >= 0.60:
        return "BULLISH lean (strong for this model)"
    if p >= 0.55:
        return "mild bullish lean"
    if p > 0.45:
        return "NO EDGE - coin flip, stay out or size tiny"
    if p > 0.40:
        return "mild bearish lean"
    return "BEARISH lean (strong for this model)"


def result_dict(res: EvalResult) -> dict:
    return asdict(res)
