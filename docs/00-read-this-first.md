# 00. Read this first

## The numbers nobody shows you in the YouTube ads

SEBI (the market regulator) publishes studies on how individual traders fare in
equity derivatives (futures and options, "F&O"):

- FY 2024-25: **91%** of individual F&O traders lost money. Total net loss about
  Rs 1.05 lakh crore. Average loss about Rs 1.1 lakh per trader.
- FY 2025-26: about **88%** lost money; aggregate loss around Rs 91,700 crore;
  average loss rose to about Rs 1.17 lakh. Participation fell 20% as people quit.
- Of traders who lost two years in a row and kept going, about **90% lost again**
  the next year. Experience alone does not fix it.
- Under-30s are now 43% of F&O traders and 89% of them lost.

Those are not "people who did it wrong". That is the population outcome of
retail short-term derivatives trading in India. Intraday cash trading is not
much better; an earlier SEBI study found 7 in 10 intraday traders lose.

## So why learn it at all?

Because the losses are concentrated in a few avoidable behaviours: trading
options with no edge, oversizing, no stop loss, revenge trading, and following
Telegram tips. A disciplined swing trader who risks 1% per trade, journals, and
sits out when there is no setup can survive long enough to learn. Surviving is
the whole first year's goal. Profit comes later, if at all.

## What this repo will and will not do

**Will:** teach you the structure of the Indian market, how to read a chart,
how to size a position so one bad trade cannot hurt you, what trading really
costs after STT and tax, and how to test an idea honestly on history before
risking money. The code shows you, with real numbers, how little predictability
there is in daily prices, and what a trend filter can and cannot do.

**Will not:** predict the market. No software does. The model here is a
teaching instrument. When it prints "P(up) = 0.69" with "AUC 0.51" beside it,
the lesson is that the 0.69 is not trustworthy. Learning to read that second
number is more valuable than the first.

## Ground rules for the first six months

1. **Cash equities only.** No options, no futures, no margin, no intraday
   leverage products. Buy shares with money you have.
2. **Paper trade for the first 30 days** (see chapter 08), then start with a
   capital you could lose entirely without changing your life. Rs 50,000 to
   Rs 2,00,000 is plenty to learn on.
3. **Risk 1% of capital per trade, maximum.** With Rs 2 lakh that is Rs 2,000.
   Position size comes from that number and your stop, never from conviction.
4. **Every trade has a written stop loss before entry.** Chapter 04.
5. **Journal every trade.** `journal/trade_journal_template.csv`. Chapter 06.
6. **Hold 2 to 15 days** (swing trading). Daily data is enough; you keep your
   day job; costs stay low; STCG tax at 20% is the same whether you hold 2 days or 11 months.
7. **No tips.** Not Telegram, not WhatsApp, not "SEBI-registered" influencers.
   If you did not do the analysis, you cannot manage the trade.
8. **Your job pays for your life; trading never has to.** The moment you need a
   trade to work, you will manage it badly.

## Reading order

| Chapter | Time |
|---|---|
| 01 Indian market basics | 40 min |
| 02 Trading styles and what fits a working person | 20 min |
| 03 Technical analysis that matters | 60 min |
| 04 Risk management (the only chapter that makes money) | 45 min |
| 05 Costs, STT and taxes | 30 min |
| 06 Trading plan and journal | 30 min |
| 07 Psychology and the classic mistakes | 30 min |
| 08 30-day learning path | reference |
| 09 How the predictor works and how to read its output | 45 min |
| 10 Glossary | reference |
