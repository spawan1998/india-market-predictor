# 08. The 30-day learning path (no real money until day 31)

About 45 minutes a day on weekdays, 2 hours on weekends.

## Week 1: structure and tools

| Day | Do |
|---|---|
| 1 | Read chapters 00 and 01. Open a demat account at a discount broker if you have none (Zerodha, Upstox, Groww, Dhan). Do **not** enable F&O. |
| 2 | Chapter 02. Set up TradingView free, add NIFTY, BANK NIFTY, India VIX, 5 stocks to a watchlist. Add SMA 50, SMA 200, EMA 20, RSI 14, volume to the daily chart template. |
| 3 | Clone this repo, install, run `imp predict`, `imp scan`, `imp backtest`. Read the output with chapter 09 open. |
| 4 | Chapter 03 first half (candles, S/R, moving averages). Mark swing highs and lows on 5 charts. |
| 5 | Chapter 03 second half (RSI, ATR, Bollinger, volume, relative strength). Compute ATR by eye vs the scanner's `atr_pct`. |
| 6-7 | Go through 20 NIFTY 50 stocks' daily charts for the last 12 months. For each, find one pullback and one breakout setup and write entry/stop/target/R result in a spreadsheet. |

## Week 2: risk and the plan

| Day | Do |
|---|---|
| 8 | Chapter 04. Run `imp size` for 10 stocks with your intended capital. Understand why volatile stocks get fewer shares. |
| 9 | Chapter 05. Open your broker's charges page and reproduce the 0.3% round-trip number for a Rs 50,000 delivery trade. |
| 10 | Chapter 06. Write your plan. Every blank filled. |
| 11 | Chapter 07. Write down which three mistakes you think you are most prone to. |
| 12 | Build your journal (copy the CSV template into Google Sheets or Excel; add a formula for R multiple and running expectancy). |
| 13-14 | Backtest by hand: pick one setup, go through 2 years of 10 stocks, log every signal (not just the good-looking ones). 40+ trades. Compute win rate, average R, expectancy. This single exercise is worth more than any course. |

## Week 3 and 4: paper trading, live market

Every day at 15:00:
1. `imp predict --symbol NIFTY50` for regime and VIX.
2. `imp scan --capital <capital> --risk 1 --top 15`.
3. Pick setups per plan, "enter" at the closing price in the journal with stop
   and target and quantity from the formula.
4. Next days: manage with the real prices. Stops hit at the open after a gap
   count as filled at the open.
5. Journal every trade including the mistake column, honestly.

Target by day 30: at least 10 paper trades fully closed, a filled-in plan, and
a journal with computed expectancy. Also read:

- *Trading in the Zone* (Mark Douglas) for psychology.
- *How to Make Money in Stocks* (William O'Neil) for breakouts and relative strength.
- Zerodha Varsity (free, zerodha.com/varsity): modules 1 to 4 and 9 for Indian
  specifics; skip the options modules for now.
- SEBI's investor education site investor.sebi.gov.in for the F&O study PDFs.

## Day 31 onward: real money, small

- Capital: an amount whose total loss would not change anything. Start at
  0.5% risk per trade.
- Trade exactly the paper plan. The only change is that it now hurts.
- After **50 live trades** (likely 4 to 8 months) do the first real review:
  expectancy, plan-adherence gap, setup ranking. Only then consider raising
  risk to 1% or adding a setup.
- After **12 months profitable net of costs and tax**, and a journal that
  shows plan adherence above 90%, you may read about futures for hedging.
  Not before. If after 12 months you are not profitable, that is the normal
  outcome; keep the SIP, keep the journal, trade smaller or stop. No shame in
  either.

## Milestones to be proud of

- First month with zero plan violations (not first profitable month).
- First -1R loss taken calmly at the stop.
- First +3R trade where you held through a scary pullback because the stop said so.
- First month where you did not trade at all because NIFTY was below the SMA-200.
