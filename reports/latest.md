## NIFTY50 daily read: 2026-10-28

Close **22,698.85** (2026-10-28). Model P(up over next 5 sessions) = **0.428**: mild bearish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3663 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.09 | 572 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.7% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ETERNAL    |   326   |     4.4 |      53 |     -2.7 |     11.1 |            -2.1 |       3.1 |
| BHARTIARTL |  1948.1 |     3.8 |      63 |      9.1 |      7.8 |            -1.6 |       2.3 |
| DRREDDY    |  1335.4 |     3.8 |      73 |     11.2 |     23   |            -0.2 |       2.4 |
| JSWSTEEL   |  1241.2 |     3.5 |      51 |     -2.8 |      4.9 |            -2.7 |       2.7 |
| KOTAKBANK  |   440   |     3.4 |      58 |      8.9 |     19.6 |            -2.9 |       2.1 |
| TECHM      |  1776.6 |     3.3 |      67 |     15.7 |     14.9 |            -3.7 |       3.1 |
| CIPLA      |  1365.6 |     3.2 |      56 |     -2.4 |     -0.1 |            -2.6 |       2.1 |
| LT         |  3801.3 |     3   |      56 |     -1.9 |      4.6 |            -2.4 |       2.2 |
| TATACONSUM |  1000.2 |     2.9 |      56 |      1.7 |     -2.2 |            -1.1 |       2.5 |
| TRENT      |  2913.9 |     2.9 |      57 |      9.2 |      4.8 |            -3   |       2.7 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| JIOFIN    |  205.15 |       0 |      31 |     -9.6 |     -7.9 |
| NTPC      |  303.75 |       0 |      37 |     -7   |     -5.3 |
| NESTLEIND | 1168    |       0 |      27 |    -14.3 |    -16.3 |
| TMPV      |  263.6  |       0 |      31 |     -9.2 |    -13.4 |
| TITAN     | 4337.9  |       0 |      34 |    -11.2 |     -5.2 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
