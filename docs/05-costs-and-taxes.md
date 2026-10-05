# 05. Costs, STT and taxes (India, FY 2026-27)

Rates below are as of the Union Budget 2026 and the April 2026 changes.
Verify on your broker's charges page and the Income Tax site before filing;
these change every budget.

## Per-trade charges on NSE cash equity

| Charge | Delivery | Intraday |
|---|---|---|
| STT (Securities Transaction Tax) | 0.1% on buy **and** sell | 0.025% on sell only |
| Exchange transaction charge | about 0.00297% | same |
| SEBI turnover fee | 0.0001% | same |
| Stamp duty | 0.015% on buy | 0.003% on buy |
| GST | 18% on brokerage + exchange charges | same |
| Brokerage | Rs 0 to Rs 20 per order at discount brokers | Rs 20 or 0.03% |
| DP charge | about Rs 15 + GST per stock per sell day | none |

Rough total for a **delivery round trip**: about **0.25% to 0.30%** of trade
value, dominated by STT. Add slippage (the gap between the price you saw and
the price you got), realistically 0.05 to 0.15% each way in NIFTY 50 names, and
you are at **0.4%** round trip. The backtester's default `--cost-bps 20` per
switch (0.2% per side) is this number.

What that means: a swing trade targeting 4% has costs eating 10% of its
target. An intraday trade targeting 0.5% has costs eating 30 to 50% of it.
Costs are why intraday is a losing game for almost everyone and why the model's
long/flat rule, with 800 switches in 15 years, loses even when its hit rate is
above 50%.

## F&O charges (for reference; you are not trading these yet)

Budget 2026 raised STT on futures from 0.02% to **0.05%** of the sell-side
turnover and on options from 0.1% to **0.15%** of the premium sold (0.15% on
the intrinsic value when exercised). SEBI also raised minimum lot values to
Rs 15 lakh. These changes were made explicitly to slow retail losses.

## Income tax

Classification depends on what you did, not what you call it:

| Activity | Head | Rate |
|---|---|---|
| Delivery, held under 12 months | Short-term capital gains (STCG), section 111A | **20%** flat + cess |
| Delivery, held 12 months or more | Long-term capital gains (LTCG), section 112A | **12.5%** above Rs 1.25 lakh per year |
| Intraday (buy and sell same day) | Speculative business income | your slab rate |
| F&O | Non-speculative business income | your slab rate |

Notes that matter for a salaried swing trader:

- STCG at 20% applies regardless of your slab, and you cannot set STCG off
  against salary. Short-term capital losses can be set off against any capital
  gains and carried forward 8 years if you file by the due date.
- Dividends are taxed at slab; TDS at 10% above Rs 10,000 per company per year.
- If you also do intraday, that is "business", you must file ITR-3 and may
  need books of account and (above turnover thresholds) a tax audit. Another
  reason to stay delivery-only: ITR-2 and done.
- Advance tax applies if total tax due exceeds Rs 10,000; capital gains are
  paid in the instalment after they arise.
- Brokers give a tax P&L report with STT already shown; download it in April.

## Hidden costs

- **Opportunity cost** of capital sitting in a trading account at 0%. Park idle
  cash in a liquid fund or a broker's instant-redeem liquid ETF.
- **Your time**: 20 minutes a day is fine; 3 hours a day watching a screen
  during work is a cost you cannot see on a contract note.
- **Subscriptions**: TradingView free tier plus this repo is enough. Paid
  "premium" indicators and Telegram channels have negative expected value.

## Worked example

Rs 2,00,000 capital, 50 swing trades a year, average Rs 45,000 per position,
0.4% round trip cost = Rs 180 per trade = Rs 9,000 a year, or 4.5% of capital.
Your edge has to pay this first. If your net result is Rs 30,000 profit, STCG
takes Rs 6,000 plus cess, leaving Rs 24,000: 12% on capital for 50 trades of
disciplined work. The NIFTY index fund did about 10 to 12% a year with zero
work. Be honest with yourself about that comparison every December.
