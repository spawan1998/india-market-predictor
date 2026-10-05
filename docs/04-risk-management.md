# 04. Risk management: the only chapter that makes money

Entries get all the attention. Risk management is what separates the 10% who
survive from the 90% in SEBI's reports. Everything here is mechanical. Follow it
mechanically.

## The R unit

Decide, before entry, the rupees you will lose if the stop is hit. That is
**1R**. With Rs 2,00,000 capital and 1% risk, 1R = Rs 2,000. Every trade is
then measured in R: a win that makes Rs 4,000 is +2R, a loss at the stop is
-1R. Your P&L over a year is the sum of R multiples times R. Thinking in R
removes rupee emotion and makes trades comparable.

## Position sizing formula

```
risk per share  = entry - stop
quantity        = floor( (capital x risk%) / risk per share )
cap             = quantity x entry <= 25% of capital
```

Example: capital 2,00,000, risk 1%, RELIANCE entry 1,450, ATR 28, stop 2 ATR
below = 1,394. Risk per share 56. Quantity = 2,000 / 56 = 35 shares, worth
Rs 50,750, which is right at the 25% cap. Run:

```
imp size --entry 1450 --atr 28 --capital 200000 --risk 1
```

Notice what the formula does: a volatile stock gets a smaller quantity, a calm
one gets more. Your loss if wrong is the same Rs 2,000 either way. You never
again ask "how many shares should I buy"; the stop answers.

## Stops

- Placed **before** entry, as a GTT/SL-M order, not in your head.
- Based on the chart (below the pullback low / breakout range) or on
  volatility (2 ATR), whichever is **nearer** to entry when sizing, but not so
  near that normal noise hits it. Under 1 ATR is noise.
- Never widened. A stop moves only toward profit (trailing).
- Honour gaps: if the stock opens below your stop, exit at the open. Do not
  wait for it to "come back". The stop was the plan; the gap is the market
  telling you the plan was wrong faster than expected.

## Targets and trailing

- Minimum reward to risk **2:1** at entry, else skip the trade. If entry is
  1,450 and stop 1,394 (R = 56), the first target must be at least 1,562, and
  there must be no obvious resistance before it.
- Take half at 2R, move the stop to breakeven, trail the rest below each new
  higher low or with a 2 ATR trailing stop. This single rule turns a 45% win
  rate into a profitable system.

## Portfolio-level limits

- **Max 1% risk per trade.** Beginners: 0.5%.
- **Max 4 to 5 open positions**, so total open risk is 4 to 5% of capital.
- **Correlated positions count as one.** Three private banks is one trade.
- **Daily loss limit**: if you lose 2R in a day, stop opening trades. Weekly:
  4R. Monthly: 6R, then stop for the month and review the journal.
- **Drawdown rule**: at 10% account drawdown, halve position sizes until back
  at the high. At 20%, stop trading real money for a month.

## Expectancy: why win rate is not the goal

```
expectancy per trade (in R) = win% x avg win(R) - loss% x avg loss(R)
```

| win rate | avg win | avg loss | expectancy |
|---|---|---|---|
| 70% | 0.5R | 1R | +0.05R (barely; options sellers live here until the blow-up) |
| 45% | 2R | 1R | +0.35R |
| 35% | 3R | 1R | +0.40R |

With costs around 0.1R per trade, you need expectancy well above 0.1R. That is
why 2:1 minimum reward to risk is non-negotiable, and why cutting winners
early (the most common retail habit) kills accounts that have a perfectly good
entry method.

## Risk of ruin

Risking 10% per trade, a run of 7 losses (which *will* happen with a 45% win
rate; probability of a 7-loss streak in 100 trades is over 50%) takes you down
52%. You then need +108% to recover. Risking 1%, the same streak costs 6.8%
and needs +7.3% to recover. Survival is about streaks, not averages.

## Leverage

Intraday products offer 5x. That turns your 1% risk per trade into 5% without
you noticing. With 5x leverage a 20% adverse move wipes the account, and NIFTY
50 stocks move 20% in a few weeks more often than you think (2020, 2022, 2024,
2025, 2026). The rule for the first year is simply: none.

## Checklist before every order

1. Setup matches one of my three written setups? (chapter 02)
2. Weekly trend agrees?
3. Stop defined from the chart, at least 1 ATR away?
4. Reward:risk at least 2:1 to the first target?
5. Quantity from the formula, under the 25% cap?
6. Total open risk after this trade under 5%?
7. Not correlated with an existing position?
8. Not a result of a tip, a loss I want back, or boredom?
9. GTT stop placed immediately after fill?
10. Journal row written before the entry order?

If any answer is no, there is no trade. Most days there is no trade.
