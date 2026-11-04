## NIFTY50 daily read: 2026-11-04

Close **23,960.60** (2026-11-04). Model P(up over next 5 sessions) = **0.713**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.500, always-up baseline 0.568 over 3668 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.9% | -46.0% | -0.08 | 573 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +11.1% | -38.4% | 0.75 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ADANIPORTS |  1910   |     4.9 |      67 |      7.7 |     14.6 |            -0.6 |       2.6 |
| KOTAKBANK  |   459.4 |     4.7 |      64 |     10.4 |     18.1 |            -1.4 |       2.1 |
| JSWSTEEL   |  1343   |     4.5 |      66 |      8.7 |      6   |             0   |       2.5 |
| GRASIM     |  3138   |     4.4 |      64 |      5.6 |      3   |            -0.1 |       2.1 |
| TRENT      |  3060   |     4.3 |      64 |     18.6 |      1.1 |            -0.1 |       2.7 |
| TITAN      |  4754.4 |     4.2 |      65 |      3.8 |     -1   |             0   |       2.3 |
| CIPLA      |  1402   |     4.2 |      65 |      5   |     -1.3 |             0   |       2   |
| INDIGO     |  5140.8 |     4.1 |      67 |      4.2 |     -1.4 |            -0.3 |       2.5 |
| EICHERMOT  |  7420   |     4   |      57 |      5.7 |     -3.8 |            -0.4 |       2.2 |
| ETERNAL    |   344.5 |     3.6 |      61 |      7.4 |     12.9 |            -1.6 |       2.9 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HDFCLIFE  |   532.5 |     1.4 |      50 |      0.3 |      2   |
| TMPV      |   278.5 |     1.3 |      49 |     -3.5 |    -17.4 |
| AXISBANK  |  1232   |     1.3 |      50 |      0.8 |      0.3 |
| TMCV      |   402.8 |     1.3 |      43 |     -5.6 |     -7.2 |
| NESTLEIND |  1248   |     1   |      47 |     -3.8 |    -15.2 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
