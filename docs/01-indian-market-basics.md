# 01. Indian market basics

## Exchanges, indices, regulator

- **NSE** (National Stock Exchange) carries over 90% of cash and almost all
  derivatives volume. **BSE** is older and has more listed companies but far
  less liquidity. Trade on NSE unless a stock is BSE-only.
- **NIFTY 50**: the 50 largest, most liquid NSE stocks, free-float market-cap
  weighted. Rebalanced in March and September. Yahoo symbol `^NSEI`.
- **BANK NIFTY**: 12 bank stocks; the most traded derivatives index. `^NSEBANK`.
- **SENSEX**: BSE's 30-stock index. `^BSESN`.
- **India VIX**: expected 30-day NIFTY volatility implied by option prices.
  Below 12 is calm, 15-20 is normal, above 25 is fear. `^INDIAVIX`.
- **SEBI** regulates everything. Brokers, advisers and research analysts need
  SEBI registration; "RA" or "IA" numbers can be checked on sebi.gov.in.
- Clearing and settlement: NSE Clearing. Depositories: **NSDL** and **CDSL**
  hold your shares in a demat account; your broker is just the interface.

## Timings (IST, Monday to Friday)

| Session | Time | What happens |
|---|---|---|
| Pre-open | 09:00 - 09:08 | Orders collected, no matching |
| Pre-open match | 09:08 - 09:15 | Equilibrium opening price computed |
| Normal | 09:15 - 15:30 | Continuous trading |
| Closing | 15:40 - 16:00 | Trades at the official close price |
| Post-close | after 16:00 | Nothing you need |

The first 15 to 30 minutes and the last 30 minutes carry most of the volume
and the worst slippage. A swing trader can place orders at 15:15 for the close
or at 09:25 after the open settles, and ignore the rest of the day.

Market holidays are published by NSE each December; about 14 to 16 per year.
Muhurat trading is a one-hour symbolic session on Diwali evening.

## Settlement

Cash equity settles **T+1**: buy on Monday, shares in demat Tuesday. Sell on
Monday, cash usable for buying immediately (80% same day with most brokers),
fully withdrawable Tuesday. Optional **T+0** settlement exists for some stocks
since 2024; irrelevant for you.

Selling shares you bought today is **intraday** (squared off automatically by
15:20 if you used the intraday product). Selling shares from demat is
**delivery**. The STT and tax treatment differ sharply (chapter 05).

## Order types

- **Market**: fills now at whatever price is available. Fine for NIFTY 50
  stocks; dangerous in illiquid names.
- **Limit**: fills only at your price or better. Default for entries.
- **Stop-loss (SL)**: becomes a limit order when the trigger price trades.
  **SL-M**: becomes a market order at the trigger. Use SL-M for stops so you
  are out; a limit stop can be skipped in a gap.
- **GTT** (Good Till Triggered): a standing stop or target that survives
  across days. Zerodha, Upstox, Groww and others support it. Swing traders
  live on GTT; place the stop the moment the entry fills.
- **AMO** (After Market Order): queue orders after hours; they go in at the
  pre-open.

## Products at a broker

- **CNC / Delivery**: pay full price, shares to demat. Use this.
- **MIS / Intraday**: leverage up to about 5x, auto-squared-off. Avoid for the
  first year.
- **MTF** (Margin Trading Facility): borrow against shares at 10-18% a year.
  Avoid.
- **F&O**: futures and options; lot-based, mark-to-market margin, weekly
  expiries on NIFTY (Tuesday) and monthly on others. SEBI keeps raising lot
  sizes and margins specifically to protect retail. Avoid until you have a
  year of profitable cash swing trades in your journal.

## Circuit limits and bands

Individual stocks have daily price bands (2%, 5%, 10%, 20%) depending on
liquidity; F&O stocks have no band but a dynamic one. Indices halt the market
at 10%, 15%, 20% moves. A stock "hitting upper circuit" cannot be bought; a
stock at lower circuit cannot be sold. Small caps trapped in lower circuits for
weeks are how retail money dies. Stick to NIFTY 50 / NIFTY 200 names.

## Who moves the market

- **FII/FPI** (foreign institutions): the marginal buyer or seller; their daily
  net flow is published every evening and drives sentiment. Rupee weakness and
  US bond yields rising usually mean FII selling.
- **DII** (domestic institutions, mostly mutual funds via SIP flows): the
  steady buyer that has cushioned FII exits since 2020.
- **Retail**: you. Roughly 10 crore demat accounts, hugely active in options.
- **Global cues**: S&P 500 overnight, US CPI and Fed decisions, crude oil
  (India imports 85%), USD/INR, and the GIFT Nifty futures price before the
  open (the old SGX Nifty).

## Market phases you must learn to recognise

1. **Trending up**: higher highs, higher lows, price above a rising 50 and
   200-day average. Buy pullbacks; breakouts work.
2. **Trending down**: the mirror. Breakouts fail; "cheap" gets cheaper. Cash
   is a position.
3. **Range / chop**: price oscillates between support and resistance; moving
   averages flat. Breakouts fail, mean reversion works, most traders lose.

The 200-day SMA line in the predictor's charts is the single most useful
regime indicator. Run `imp backtest` to see what being long only above it does
to drawdowns.

## Where to look things up

- nseindia.com: official prices, FII/DII data, corporate actions, holidays.
- screener.in: fundamentals of any listed company, free.
- tradingview.com: charts (free tier is enough; NSE data included).
- chartink.com: free technical screener for NSE.
- sebi.gov.in: registered intermediaries check; investor charter.
- Your broker's app for execution only. Do not analyse there; the app is
  built to make you trade more.
