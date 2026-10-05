"""Charts and a Markdown daily report.

Charts follow a restrained style: thin lines, one y-axis per chart, muted grid,
direct labels, a legend when there is more than one series.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

from .features import sma  # noqa: E402

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"

# Palette: series-1 blue, series-2 orange, series-3 aqua; muted ink for chrome.
BLUE, ORANGE, AQUA, VIOLET = "#2a78d6", "#eb6834", "#1baf7a", "#4a3aa7"
INK, MUTED, GRID, SURFACE = "#0b0b0b", "#898781", "#e1e0d9", "#fcfcfb"


def _style(ax, title: str):
    ax.set_facecolor(SURFACE)
    ax.set_title(title, loc="left", color=INK, fontsize=11, pad=10)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=MUTED, labelsize=8)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)


def _label_end(ax, series: pd.Series, text: str, color: str):
    ax.annotate(text, (series.index[-1], series.iloc[-1]), xytext=(6, 0),
                textcoords="offset points", va="center", fontsize=8, color=INK)


def price_chart(df: pd.DataFrame, probs: pd.Series | None, name: str, path: Path, lookback: int = 250):
    d = df.iloc[-lookback:]
    c = d["Close"]
    fig, axes = plt.subplots(2, 1, figsize=(10, 6.5), sharex=True,
                             gridspec_kw={"height_ratios": [3, 1], "hspace": 0.25})
    fig.patch.set_facecolor(SURFACE)
    ax = axes[0]
    ax.plot(c.index, c, color=BLUE, linewidth=1.6, label="Close")
    s50, s200 = sma(df["Close"], 50).iloc[-lookback:], sma(df["Close"], 200).iloc[-lookback:]
    ax.plot(s50.index, s50, color=ORANGE, linewidth=1.2, label="SMA 50")
    ax.plot(s200.index, s200, color=AQUA, linewidth=1.2, label="SMA 200")
    _label_end(ax, c, f"{c.iloc[-1]:,.0f}", BLUE)
    ax.legend(frameon=False, fontsize=8, loc="upper left", labelcolor=INK)
    _style(ax, f"{name}: last {lookback} sessions with 50/200-day averages")

    ax2 = axes[1]
    if probs is not None:
        p = probs.reindex(d.index)
        ax2.plot(p.index, p, color=BLUE, linewidth=1.4)
        ax2.axhline(0.5, color=MUTED, linewidth=0.8, linestyle="--")
        ax2.axhspan(0.45, 0.55, color=GRID, alpha=0.6, linewidth=0)
        ax2.set_ylim(0.2, 0.8)
        _style(ax2, "Model P(up over horizon): grey band = no edge")
    else:
        ax2.set_visible(False)
    fig.savefig(path, dpi=140, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    return path


def equity_chart(curves: pd.DataFrame, name: str, path: Path):
    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.patch.set_facecolor(SURFACE)
    series = [("ml", BLUE, "ML long/flat"), ("buy_and_hold", ORANGE, "Buy and hold"),
              ("sma200", AQUA, "SMA-200 filter"), ("combo", VIOLET, "ML + SMA-200")]
    for col, color, label in series:
        if col in curves:
            ax.plot(curves.index, curves[col], color=color, linewidth=1.4, label=label)
            _label_end(ax, curves[col], f"{curves[col].iloc[-1]:.2f}x", color)
    ax.set_yscale("log")
    from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator
    ax.yaxis.set_major_locator(FixedLocator([0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}x"))
    ax.legend(frameon=False, fontsize=8, loc="upper left", labelcolor=INK)
    _style(ax, f"{name}: growth of 1 unit, out-of-sample, after costs (log scale)")
    fig.savefig(path, dpi=140, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    return path


def importance_chart(imp: pd.Series, path: Path, top: int = 15):
    top_imp = imp.head(top)[::-1]
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor(SURFACE)
    ax.barh(top_imp.index, top_imp.values, color=BLUE, height=0.6)
    ax.grid(axis="x", color=GRID, linewidth=0.6)
    ax.grid(axis="y", visible=False)
    _style(ax, "Which features the model leans on (permutation importance, AUC drop)")
    ax.grid(axis="y", visible=False)
    fig.savefig(path, dpi=140, bbox_inches="tight", facecolor=SURFACE)
    plt.close(fig)
    return path


def write_markdown(path: Path, sections: list[tuple[str, str]]):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    body = "\n\n".join(f"## {title}\n\n{text}" for title, text in sections)
    path.write_text(body + "\n", encoding="utf-8")
    return path
