## NIFTY50 daily read: 2026-10-30

Close **23,053.10** (2026-10-30). Model P(up over next 5 sessions) = **0.376**: BEARISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3665 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.09 | 572 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.9% | -38.4% | 0.74 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| KOTAKBANK  |  461.6  |     4.9 |      69 |     13.7 |     23.7 |            -0.3 |       2.1 |
| ETERNAL    |  343.65 |     4.8 |      62 |      4.8 |     15.8 |            -0.8 |       3.1 |
| ADANIPORTS | 1850    |     4.8 |      61 |      1.5 |     16.4 |            -1.2 |       2.8 |
| TRENT      | 3017.3  |     4.3 |      62 |     14.5 |      5.8 |            -1.4 |       2.9 |
| CIPLA      | 1378.9  |     4.2 |      59 |     -0   |     -0.8 |            -0.2 |       2.1 |
| JSWSTEEL   | 1246    |     3.6 |      52 |     -2.1 |      3.2 |            -1.6 |       2.6 |
| INFY       | 1185    |     3.4 |      64 |     16.7 |      7.8 |            -1.1 |       3.5 |
| GRASIM     | 2981.4  |     3.4 |      50 |     -3.8 |      1.5 |            -2.1 |       2.1 |
| TECHM      | 1790.8  |     3.3 |      68 |     19.5 |     13.4 |            -2.9 |       3   |
| DRREDDY    | 1352    |     3.3 |      75 |      8   |     23.3 |            -0.9 |       2.2 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HINDALCO  |   884.7 |     0.1 |      39 |     -7.4 |     -3.6 |
| NESTLEIND |  1167   |     0   |      30 |    -13.3 |    -18.1 |
| JIOFIN    |   204.5 |     0   |      33 |     -6   |    -11.8 |
| TATASTEEL |   167.6 |     0   |      34 |    -10.9 |     -5.1 |
| TMPV      |   265.4 |     0   |      34 |     -5.5 |    -15.4 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
