# 03. Technical analysis that actually matters

Technical analysis is not prediction. It is a shared language for describing
where buyers and sellers have acted, so you can place stops and targets at
levels that mean something. Learn these and ignore the rest.

## Candles and bars

Each daily candle: open, high, low, close. The body is open-to-close; the
wicks are the extremes. What matters:
- **Close position in the range** (the predictor's `close_pos` feature): a
  close near the high means buyers won the day.
- **Range relative to recent days**: wide-range days on volume mark decisions;
  narrow-range days mark indecision and often precede breakouts.
- **Gaps** (`gap` feature): open far from the previous close. In uptrends
  gaps up often fill partially then continue; in downtrends gaps down rarely fill fast.

Do not memorise 40 candlestick patterns. "Reversal bar" (closes above prior
high after a pullback) and "wide-range breakout bar" cover 90% of swing entries.

## Support, resistance, swing highs and lows

Mark the last 3 to 4 swing highs and swing lows on a daily chart. Price
remembers them because people who bought there remember them. Stops go
*beyond* these levels (below support for longs), not at them, because
everyone's stops cluster there and get hunted.

## Trend: moving averages

- **SMA 200**: the regime line. Above and rising = bull regime. Below = bear.
  Institutional desks watch it, so it is self-fulfilling.
- **SMA 50**: intermediate trend. Pullbacks in strong stocks hold the 50.
- **EMA 20**: short-term trend. Momentum stocks ride it.
- **Stacked** (price > 20 > 50 > 200, all rising) = the strongest configuration.
  The scanner gives full trend points only for 50 > 200 with price above both.
- **Golden / death cross** (50 crossing 200): lagging; mostly useful as a
  regime label, not a trade trigger.

## Momentum: RSI

RSI(14) measures the speed of recent gains vs losses, 0 to 100.
- In a **range**: above 70 overbought (fade), below 30 oversold (buy). Works.
- In a **trend**: RSI stays 50 to 80 for months in uptrends. "Overbought" is a
  reason to hold, not sell. In downtrends it stays 20 to 50.
- Best use for swing: pullback entries when RSI dips to 40-50 in an uptrend
  (the scanner's `rsi_ok` component rewards 45 to 70).
- **Divergence**: price makes a new high, RSI does not. A warning, not a signal.

## MACD

Difference between 12 and 26-day EMAs, with a 9-day signal line. Histogram
turning up from below zero in an uptrend is a decent pullback-end confirmation.
Alone, it whipsaws in ranges; the model's `macd_cross` feature exists to let the
data decide how useful it is (spoiler: a little).

## Volatility: ATR and Bollinger Bands

- **ATR(14)**: average daily true range in rupees. This is your unit of
  distance. Stops at 2 ATR, targets at 4 ATR, position size from ATR. A stock
  with ATR 2% of price moves 2% on a normal day; a 1% stop will be hit by noise.
- **Bollinger Bands** (20-day SMA plus or minus 2 standard deviations):
  bandwidth squeezing to multi-month lows precedes expansions (breakouts);
  `%B` above 1 means closing above the upper band, which in trends is strength.

## Volume

Volume confirms. Breakouts on 1.5 to 2x average volume hold; breakouts on thin
volume fail. Pullbacks on declining volume are healthy. The scanner's
`vol_trend` is the 5-day average over the 20-day average. Index volume on Yahoo
is unreliable, so the model only uses volume for stocks.

## Relative strength (not RSI)

Stock return minus index return over 1 to 3 months. Leaders outperform in dips
and lead on the recovery. This is the best-documented anomaly in equity markets
(momentum) and the backbone of the scanner's ranking. Buy strength, not "cheap".

## Multiple timeframes

Weekly chart for direction, daily chart for entry. Never take a daily long in a
stock whose weekly chart is in a clear downtrend.

## What to ignore

Fibonacci levels, Elliott waves, Gann, harmonic patterns, 90% of indicators,
anyone drawing 12 lines on a chart, "option chain analysis" videos, and any
indicator that is a transformation of price labelled as a new source of information.

## Practise

Open TradingView, pull up any NIFTY 50 stock, daily, 1 year. Add SMA 50, SMA
200, EMA 20, RSI 14, volume. Mark swing highs and lows. Find one pullback
setup and one breakout setup from the last year. Write down, for each: entry,
stop, target, and the R-multiple result. Do this for 20 stocks before you place
a trade. That is week 2 of the learning path.
