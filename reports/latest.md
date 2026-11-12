## NIFTY50 daily read: 2026-11-12

Close **25,255.05** (2026-11-11). Model P(up over next 5 sessions) = **0.618**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.500, always-up baseline 0.568 over 3672 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.5% | -46.0% | -0.05 | 573 |
| sma200 | +4.2% | -28.6% | 0.43 | 123 |
| combo | -3.5% | -51.2% | -0.37 | 485 |
| buy_and_hold | +11.5% | -38.4% | 0.77 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |    close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|---------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| JSWSTEEL   |  1353.3  |     4.1 |      66 |     15.9 |      1.2 |            -1.2 |       2.3 |
| ADANIPORTS |  1907    |     4.1 |      62 |      8.3 |     10.7 |            -3.6 |       2.8 |
| CIPLA      |  1419.9  |     4   |      68 |      9.1 |     -6   |            -0.1 |       1.8 |
| BAJAJ-AUTO | 11040    |     3.9 |      64 |     12.9 |     -8.2 |            -0.7 |       2.3 |
| BAJFINANCE |  1078.8  |     3.8 |      68 |     12.4 |     -4.9 |            -1   |       2.8 |
| APOLLOHOSP |  8604    |     3.8 |      61 |      7.2 |     -6.1 |            -1.1 |       2.4 |
| TMCV       |   446.05 |     3.8 |      64 |      8.7 |     -3.7 |            -1.5 |       3.4 |
| BHARTIARTL |  2109    |     3.7 |      71 |     16.8 |      5.8 |            -0.5 |       2.2 |
| AXISBANK   |  1336.4  |     3.6 |      69 |      6.1 |      4.4 |            -1.8 |       2.3 |
| GRASIM     |  3156.7  |     3.5 |      61 |      9.2 |     -9.4 |            -2.5 |       2.2 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| TATACONSUM |  1093   |     1.7 |      72 |     14.5 |     -4.1 |
| MAXHEALTH  |   928.3 |     1.7 |      58 |      5   |    -15.9 |
| BAJAJFINSV |  1845   |     1.7 |      64 |      6.4 |    -11.5 |
| INFY       |  1155   |     1.4 |      59 |     15.4 |     -2.9 |
| NESTLEIND  |  1288   |     1   |      54 |     -3.4 |    -18.5 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
