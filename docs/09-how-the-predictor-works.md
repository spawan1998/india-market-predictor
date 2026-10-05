# 09. How the predictor works and how to read it

## The question it answers

"Given everything knowable at today's close, what is the probability that the
close N sessions from now is higher?" N = 5 (one week) by default, matching a
swing horizon. N = 1 is next-day.

## Pipeline

```
Yahoo Finance  ->  data.py (CSV cache)  ->  features.py  ->  model.py  ->  backtest.py / cli.py
  OHLCV since 2008     daily bars            ~45 features     GBM / logit      long-flat rules, costs
  + VIX, S&P 500,                            + forward        walk-forward
    USD/INR, crude                             return label    out-of-sample
```

### Features (all computed from the past only)

- Returns over 1, 2, 3, 5, 10, 20 days; overnight gap; day range; where the
  close sat in the range.
- Distance from SMA 10/20/50/200; SMA 20 vs 50, 50 vs 200; EMA-20 slope.
- RSI 7 and 14; MACD line, histogram, and histogram sign change.
- ATR as a percentage of price; 10 and 20-day realised volatility and their ratio.
- Bollinger %B and bandwidth.
- Distance from 20-day high, 20-day low, 52-week high.
- Volume z-score and 5/20-day volume trend (stocks only; index volume is unreliable).
- Day of week; month-end flag.
- Context: India VIX level and 5-day change; S&P 500 1-day and 5-day return
  and distance from its SMA-50 (shifted one session so only the US close that
  happened *before* India's open is used); USD/INR 5-day change; crude 5-day change.

`tests/test_features.py::test_features_do_not_use_future` proves that cutting
the last 30 days off the data leaves every earlier feature row unchanged. If
you add a feature, keep that test passing.

### Label

`fwd = Close[t+N] / Close[t] - 1`; `y = 1 if fwd > 0`. The last N rows have no
label and are never used for training, only for the live prediction.

### Models

- **gbm**: `HistGradientBoostingClassifier`, 300 shallow trees (depth 3),
  learning rate 0.03, 40 samples per leaf, L2 = 1. Handles missing values.
- **logit**: median-imputed, standardised logistic regression with C = 0.1.
  Linear and heavily regularised. On most symbols it does as well as the GBM,
  which tells you the signal, where it exists, is simple.

### Walk-forward evaluation (why the numbers are believable)

Starting after 750 sessions (about 3 years), the model is trained on all data
up to T minus N (the N-session gap stops label leakage), predicts the next 63
sessions, then rolls forward and retrains. About 58 retrains cover 2011 to
today. Every probability in the "out-of-sample" record was produced by a model
that had never seen that day or anything after it. Metrics reported:

- **accuracy**: share of correct up/down calls at 0.5.
- **balanced accuracy**: average of up-recall and down-recall; immune to the
  fact that markets rise about 57% of weeks.
- **AUC**: probability that a random up-week got a higher score than a random
  down-week. 0.50 = coin flip. 0.53 to 0.56 is a real but small edge. Above
  0.60 on an index means a bug.
- **always-up baseline**: the accuracy you get by predicting "up" every time.
  If the model is below it, the model has no information you can use directly.

### Backtest

Four strategies on the out-of-sample window, each paying `--cost-bps` per
position change (default 20 bps, chapter 05):

- **ml**: long when P(up) rises above `--threshold` (0.55), flat when it
  falls below threshold minus `--hysteresis` (0.05). Hysteresis stops the
  signal flipping daily and halves costs.
- **sma200**: long when close is above its 200-day SMA. The classic.
- **combo**: long only when both say long.
- **buy_and_hold**: the benchmark that most active strategies fail to beat.

Reported: total return, CAGR, Sharpe (annualised mean/std of daily returns),
maximum drawdown, time in market, number of switches, hit rate of days held.

## Reading `imp predict` output

```
NIFTY50  close 22,553.80 on 2026-10-05
P(up over next 5 sessions) = 0.690  ->  BULLISH lean (strong for this model)
Walk-forward (out-of-sample, 3647 predictions, 58 retrains):
  accuracy 0.526   balanced 0.499   AUC 0.506
  'always up' baseline 0.568
No proven edge on this symbol: out-of-sample AUC is ~0.5 ...
Trend filter: close is BELOW the 200-day SMA (23,850).
```

How to read that, line by line:

1. P(up) = 0.69 looks confident.
2. AUC 0.506 says the model's confident calls have been right about as often
   as its unconfident ones. The 0.69 therefore carries almost no information.
3. Balanced accuracy 0.499 confirms it: it is not telling up from down.
4. Accuracy 0.526 is below the 0.568 you would get by always saying "up".
5. The yellow note states all of this in one sentence.
6. The trend filter says NIFTY is below its 200-day SMA. Per the plan, no new
   longs. This line is doing the real work.

So the action from this output is: **no new long positions; keep stops on
existing ones**. The 0.69 is a lesson in why probabilities need a track record
beside them.

When you run the model on single stocks or at horizon 1, you will sometimes
see AUC 0.53 to 0.55 and the note turns green. That is a small real edge,
usually momentum, and it is still worth only a tilt in position selection, not
a reason to abandon stops or sizing.

## Why the ML rule loses to buy-and-hold on NIFTY

- The edge is near zero, so the rule is roughly a coin flip about when to be
  in the market.
- Being out of the market half the time forfeits the equity risk premium
  (NIFTY's drift of about 10 to 12% a year) and the big up days, which cluster
  right after big down days.
- 800 switches at 20 bps is about 160% of capital paid in costs over 15 years.

The SMA-200 filter loses to buy-and-hold on return too, but usually cuts the
maximum drawdown substantially. That is the honest value proposition of trend
following: smaller crashes, not bigger gains. Whether that trade is worth it is
a personal choice about how much drawdown you can live through without quitting.

## Extending it (good exercises)

- Add a feature (FII net flows from NSE, GIFT Nifty gap, sector momentum) and
  see if AUC moves. Keep the no-leak test passing.
- Try horizon 10 or 20 (monthly momentum is better documented than weekly).
- Run on 20 stocks and compare AUC; single-stock momentum is usually stronger
  than index timing.
- Add the scanner's score as a feature for stock-level models.
- Build a cross-sectional model: rank all NIFTY 50 stocks by predicted
  5-day return and hold the top 5. That is a real, published strategy family
  (cross-sectional momentum); test it honestly with costs.
- Calibrate probabilities (`CalibratedClassifierCV`) so 0.69 means 69%.

## Limitations

- Yahoo data: daily, adjusted for splits and dividends, occasionally missing a
  day; index volume is junk; new symbols after demergers (TMPV, TMCV) have
  short histories.
- No intraday, no order book, no options data, no fundamentals, no news.
- Survivorship: the NIFTY 50 list is today's list; stocks that fell out are
  not in the scan. The index model itself has no survivorship problem.
- The model is retrained quarterly in the walk-forward but on the live
  prediction it is trained on everything to date; that is fine and intended.
- Nothing here accounts for your taxes, your slippage, or your discipline.
