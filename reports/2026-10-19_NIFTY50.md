## NIFTY50 daily read: 2026-10-19

Close **22,888.95** (2026-10-19). Model P(up over next 5 sessions) = **0.522**: NO EDGE - coin flip, stay out or size tiny.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3657 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.9% | -46.0% | -0.08 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.74 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| TECHM     | 1779.1  |     4.1 |      74 |     14   |     18.4 |            -1   |       2.9 |
| KOTAKBANK |  442.3  |     3.5 |      63 |      6.2 |     21.3 |            -2.4 |       2.1 |
| HCLTECH   | 1379.9  |     3.5 |      70 |     10.6 |     19.6 |            -1.4 |       2.9 |
| TCS       | 2460.9  |     3.5 |      73 |     13   |     15.5 |            -1.4 |       3   |
| ICICIBANK | 1381    |     3.4 |      55 |      2.5 |      0.9 |            -2.2 |       1.8 |
| EICHERMOT | 7349    |     3.4 |      53 |     -1.9 |      3.7 |            -2.9 |       2   |
| WIPRO     |  182.14 |     3.4 |      68 |      9.5 |     10   |            -2   |       2.6 |
| INFY      | 1130.7  |     3.1 |      62 |      6.8 |      9.6 |            -3.2 |       2.8 |
| JSWSTEEL  | 1241.3  |     3   |      51 |     -1   |      4.3 |            -4.8 |       2.4 |
| DRREDDY   | 1242.5  |     2.9 |      60 |      5.7 |      7.2 |            -0.8 |       2.1 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| INDIGO     |    4700 |       0 |      38 |     -3   |     -4.5 |
| APOLLOHOSP |    7700 |       0 |      33 |    -12.2 |     -7.9 |
| MAXHEALTH  |     830 |       0 |      23 |    -20   |    -19.1 |
| SUNPHARMA  |    1743 |       0 |      34 |     -6.7 |     -5.3 |
| TMPV       |     278 |       0 |      38 |    -11.6 |    -11.8 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
