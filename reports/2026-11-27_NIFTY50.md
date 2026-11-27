## NIFTY50 daily read: 2026-11-27

Close **25,884.50** (2026-11-26). Model P(up over next 5 sessions) = **0.575**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.492, AUC 0.501, always-up baseline 0.569 over 3682 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.4% | -46.0% | -0.04 | 573 |
| sma200 | +4.3% | -28.6% | 0.45 | 123 |
| combo | -3.3% | -51.2% | -0.34 | 485 |
| buy_and_hold | +11.7% | -38.4% | 0.78 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| TECHM      |  1854.7 |     4.8 |      67 |      3.3 |     11.2 |            -0.3 |       2.6 |
| HCLTECH    |  1468.6 |     4.5 |      67 |      3.6 |      5.2 |            -0   |       2.8 |
| APOLLOHOSP |  9222.5 |     3.8 |      69 |     17.6 |     -0.9 |            -2   |       2.2 |
| CIPLA      |  1450   |     3.7 |      67 |      7   |     -6   |            -1.5 |       2   |
| EICHERMOT  |  8180   |     3.6 |      67 |     15.2 |     -5.2 |            -2.2 |       2.5 |
| ULTRACEMCO | 12737   |     3.6 |      67 |     13.9 |      3.8 |            -1.9 |       2.1 |
| DRREDDY    |  1392   |     3.5 |      66 |      6.2 |     10.1 |            -1.2 |       1.8 |
| TCS        |  2640.3 |     3.5 |      71 |      4.2 |      9.3 |             0   |       2.8 |
| TATACONSUM |  1164   |     3.5 |      68 |     24.3 |      2.7 |            -1.8 |       2.3 |
| INFY       |  1183   |     3.5 |      63 |      3.8 |      0.2 |            -1.3 |       3.1 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| NESTLEIND | 1320.3  |     1.3 |      56 |     12.5 |    -17.1 |
| TMPV      |  262    |     1.3 |      41 |     -0.6 |    -23.5 |
| NTPC      |  320.25 |     1.2 |      53 |      7.8 |    -10.6 |
| COALINDIA |  388.9  |     1.1 |      45 |     -1.5 |     -7.6 |
| TATASTEEL |  163.54 |     1   |      36 |     -3.8 |    -19.1 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
