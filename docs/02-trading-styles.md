# 02. Trading styles, and what fits a person with a day job

| Style | Holding period | Data needed | Time per day | Costs | Realistic for you now? |
|---|---|---|---|---|---|
| Scalping | seconds to minutes | tick / 1-min | full market hours | enormous | No |
| Intraday | minutes to hours | 5-min / 15-min | 09:15 - 15:30 at the screen | high (STT, slippage, 5x leverage) | No |
| **Swing** | 2 to 15 days | daily + weekly bars | 20 min after the close | moderate | **Yes** |
| Positional | weeks to months | daily + weekly | 1 hour a week | low | Yes, later |
| Investing | years | fundamentals | occasional | lowest | Yes, separately via index funds / SIP |

## Why swing trading is the only sane "short-term" choice here

- You decide at the close with full information and no time pressure. The
  predictor and the scanner are built for exactly this moment (15:30 to 09:15).
- Daily bars are free and clean. Intraday data is noisy, and free intraday
  history barely exists.
- Costs: one entry and one exit per week, each at delivery STT 0.1%. Compare
  intraday: 5x leverage on a 0.3% move with 0.025% STT plus slippage every
  single day.
- Gap risk exists (news overnight) but is bounded if you size for it.
- Taxed as short-term capital gains at a flat 20%, not as business income at
  your slab, and no audit headaches (chapter 05).

## The three swing setups worth learning first

Keep to these three. Each has clear entry, stop and target rules, so they can
be journaled and tested.

### 1. Pullback in an uptrend
- Stock above a rising 50-day SMA, which is above the 200-day SMA.
- Price pulls back 3 to 8% toward the 20-day EMA or 50-day SMA on falling volume.
- Entry: first day that closes above the previous day's high (a "reversal bar").
- Stop: below the pullback low, or 2 ATR below entry, whichever is nearer.
- Target: prior swing high (first), then trail.

### 2. Breakout from a base
- Stock has traded in a tight range (bandwidth narrowing) for 3 to 8 weeks
  near a 52-week or 20-day high.
- Entry: close above the range high on volume at least 1.5x the 20-day average.
- Stop: back inside the range (below the breakout day's low).
- Target: range height added to breakout level, then trail.
- The scanner's `from_20d_high` and `vol_trend` columns are hunting for this.

### 3. Relative-strength leader after a market dip
- NIFTY falls 3 to 5% over a couple of weeks; a few stocks barely fall or make
  new highs (positive `rel_3m` in the scan).
- When NIFTY prints its first strong up day, buy those leaders.
- Stop: 2 ATR. This is the setup that produces the biggest winners and is the
  core of the scanner's score.

## Short-selling

In the cash market you can only short intraday (must cover by 15:20). Multi-day
shorts need futures or buying puts. For the first year: when the trend is down,
you hold cash. That is already a 50% improvement over most retail traders.

## What to expect

A good discretionary swing trader wins 40 to 55% of trades and makes the money
on asymmetry: average win about 2x average loss. A year with 50 trades, 45% win
rate, average win 2R and average loss 1R gives: 22.5 x 2R - 27.5 x 1R = 17.5R.
At R = 1% of capital that is about 17% before costs and tax. Nobody doubles an
account in a year without taking risks that eventually destroy it.
