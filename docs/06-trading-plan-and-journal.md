# 06. Trading plan and journal

## The plan (fill this in, print it, keep it next to the laptop)

```
CAPITAL            Rs ______  (money I can lose entirely)
RISK PER TRADE     ____ %     (0.5% to start, 1% after 30 journaled trades)
MAX OPEN TRADES    4
MAX OPEN RISK      4 %
INSTRUMENTS        NSE cash delivery, NIFTY 200 stocks only
HOLDING PERIOD     2 to 15 sessions
WHEN I TRADE       15:00 - 15:25 review and orders; 09:20 check gaps. Never otherwise.
REGIME FILTER      New longs only when NIFTY is above its 200-day SMA
                   (imp predict prints this line)
SETUPS             1. Pullback in uptrend  2. Base breakout  3. RS leader after dip
ENTRY              Close above prior high (pullback) / close above range on 1.5x volume (breakout)
STOP               Chart level or 2 ATR, whichever nearer; GTT SL-M placed on fill
TARGET             Half at 2R, stop to breakeven, trail rest by 2 ATR
LOSS LIMITS        Day -2R stop opening; week -4R; month -6R stop for the month
DRAWDOWN           -10% halve size; -20% paper trade for a month
REVIEW             Sunday 30 minutes: journal stats, scan, plan the week
```

A plan you did not write down does not exist. A plan you broke once is not a plan.

## The daily routine (20 minutes)

**15:00 to 15:25 IST**
1. `imp predict --symbol NIFTY50` : regime (above/below SMA-200), VIX, and the
   model's lean with its honesty note.
2. `imp scan --capital <your capital> --risk 1 --top 15` : candidates.
3. Open the top 5 on TradingView. Does any match one of the three setups
   *today*? Usually no. If yes, run the 10-point checklist (chapter 04).
4. Place entry at or near the close (limit order), GTT stop immediately.
5. Review open positions: stop hit? Target reached? Trail the stop.
6. Journal row.

**09:20 IST**
Only if you hold positions: any gap through a stop? Exit at market. Nothing else.

**Sunday**
Journal statistics, scan the weekly charts of leaders, note earnings dates
(do not hold swing positions through earnings in year one), note RBI / Fed /
budget dates.

## The journal

Template: `journal/trade_journal_template.csv`. Columns:

| column | why |
|---|---|
| date, symbol, direction | identification |
| setup | which of the three; lets you find which one actually works for you |
| entry, stop, target, qty, risk_rupees | the plan at entry; written before the order |
| exit_date, exit_price, pnl_rupees, r_multiple | the result in R |
| followed_plan | yes/no. The most important column. |
| mistake | moved stop / sized wrong / no setup / chased / tip / revenge / early exit |
| lesson | one sentence |

Attach a screenshot of the chart at entry and at exit (TradingView snapshot
link in a notes column, or a folder of PNGs named by date and symbol).

## Monthly review questions

1. Expectancy in R = sum(R) / number of trades. Positive?
2. Win rate, average win R, average loss R, biggest loss R (should be about -1R;
   a -2.5R means you ignored a stop).
3. Expectancy of trades where `followed_plan = yes` vs `no`. This gap is
   usually the whole story.
4. Expectancy by setup. Drop the worst one for a quarter.
5. Number of trades. More than 15 a month on a swing plan means overtrading.
6. Did I trade below the 200-day SMA? Result?

After 50 journaled trades you will know more about your own trading than any
course can teach. Until then, every judgment about "my edge" is a guess.
