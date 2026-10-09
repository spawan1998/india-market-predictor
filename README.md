# india-market-predictor

Learn short-term trading on the Indian market the honest way, with a tool that
shows you what is and is not predictable.

**Website:** [spawan1998.github.io/india-market-predictor](https://spawan1998.github.io/india-market-predictor/)
**Interactive chart + prediction for NIFTY, BANK NIFTY and every NIFTY 50 stock:** [app/](https://spawan1998.github.io/india-market-predictor/app/)
**Today's NIFTY read and scan:** [reports/latest](reports/latest.md) (updated every weekday after the close by GitHub Actions)
**Course:** start at [docs/00-read-this-first](docs/00-read-this-first.md)

> **Read [docs/00-read-this-first.md](docs/00-read-this-first.md) before anything else.**
> SEBI's own studies show roughly 9 in 10 retail F&O traders lose money. This repo
> exists to keep you out of that statistic, not to hand you a money printer.

## What is in here

| Part | What it does |
|---|---|
| `docs/` | A 10-chapter course: market structure, trading styles, technical analysis, risk, costs and taxes, a trading plan, psychology, a 30-day learning path, how the model works, glossary |
| `imp predict` | Walk-forward ML model giving P(price higher in N sessions) for NIFTY, BANK NIFTY or any NSE stock, with honest out-of-sample accuracy printed beside it |
| `imp backtest` | Compares the ML signal, the classic 200-day SMA trend filter, their combination and buy-and-hold, after transaction costs |
| `imp scan` | Ranks NIFTY 50 stocks by trend + momentum and prints a risk-controlled position size (entry, stop, quantity) |
| `imp size` | Position-size calculator: capital, risk %, ATR stop |
| `imp report` | Markdown report with charts in `reports/`; a GitHub Action runs it every weekday after the close |
| `journal/` | Trade journal template (the single highest-value habit) |

## Quick start

```bash
git clone https://github.com/spawan1998/india-market-predictor.git
cd india-market-predictor
uv venv --python 3.12 .venv && source .venv/bin/activate   # or python3 -m venv .venv
uv pip install -e ".[dev]" tabulate                          # or pip install -e ".[dev]" tabulate

imp predict --symbol NIFTY50 --horizon 5      # one-week direction, with walk-forward stats
imp predict --symbol RELIANCE --horizon 1     # next-day, single stock
imp backtest --symbol NIFTY50                 # ML vs SMA-200 vs buy-and-hold, after costs
imp scan --capital 200000 --risk 1 --top 10   # watchlist + position sizes for Rs 2 lakh
imp size --entry 1450 --atr 28 --capital 200000 --risk 1
imp report                                    # reports/<date>_NIFTY50.md + PNG charts
```

Data comes from Yahoo Finance (free, daily bars, 15-minute delayed quotes). The
first run downloads history since 2008 and caches it under `data/cache/`.

### Interactive app (optional)

`app.py` is a small Streamlit front end over the same code: pick a symbol and
horizon, get the probability, the walk-forward record, charts and the scan.

```bash
pip install -e ".[app]"
streamlit run app.py
```

It can be hosted free on [Streamlit Community Cloud](https://share.streamlit.io):
sign in with GitHub, pick this repo, main file `app.py`. Nothing else to configure.

## What the numbers mean

`imp predict` prints a probability **and** the model's walk-forward record on
that symbol. Every prediction in that record was made with a model that had
never seen the day it was predicting. If the AUC is around 0.50 the tool says so
in yellow: the probability is noise and you should lean on the simple trend
filter instead. Typical results on NIFTY: accuracy 52-53%, AUC 0.50-0.54. That
is the real state of the art for daily direction from price data alone, and
the reason the course spends more pages on risk management than on prediction.

## Honest results (NIFTY 50, 2011-2026, out-of-sample, 20 bps per switch)

Run `imp backtest` to reproduce (numbers from 2026-10-05; horizon 5, GBM):

| strategy | CAGR | max drawdown | Sharpe | switches |
|---|---|---|---|---|
| ML long/flat (enter > 0.55, exit < 0.50) | -1.7% | -41.7% | -0.06 | 543 |
| SMA-200 trend filter | +4.0% | -28.6% | 0.42 | 122 |
| ML + SMA-200 | -3.6% | -50.6% | -0.37 | 454 |
| Buy and hold | +10.7% | -38.4% | 0.73 | 1 |

Walk-forward AUC for the ML model on NIFTY: 0.506 (coin flip). On this data the
ML rule loses to buy-and-hold; the 200-day SMA filter gives up return for a
smaller drawdown. That trade-off, not "beating the market", is what a trend
filter is for. The course (chapters 04 and 09) explains why this is the
expected result and what to do with it.

## Layout

```
market_predictor/
  data.py       Yahoo download + CSV cache
  features.py   indicators (RSI, MACD, ATR, Bollinger, SMA distances, VIX, S&P, USDINR, crude)
  model.py      GBM and logistic models, walk-forward evaluation, permutation importance
  backtest.py   long/flat rules with costs vs buy-and-hold
  scan.py       NIFTY 50 trend/momentum screen + position sizing
  report.py     charts and markdown report
  cli.py        the `imp` command
docs/           the course
tests/          leak and sizing tests (pytest)
.github/        daily report workflow
```

## Disclaimer

Educational software. Not investment advice, not SEBI-registered research. Past
backtests do not predict future returns. You alone are responsible for your trades.
