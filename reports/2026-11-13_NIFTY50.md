## NIFTY50 daily read: 2026-11-13

Close **25,144.30** (2026-11-13). Model P(up over next 5 sessions) = **0.675**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.501, always-up baseline 0.568 over 3674 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.6% | -46.0% | -0.05 | 573 |
| sma200 | +4.1% | -28.6% | 0.43 | 123 |
| combo | -3.5% | -51.2% | -0.37 | 485 |
| buy_and_hold | +11.5% | -38.4% | 0.77 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| CIPLA      | 1391.8  |     3.6 |      55 |      4.7 |     -7.8 |            -2.1 |       1.8 |
| AXISBANK   | 1331    |     3.6 |      66 |      4.9 |      5.3 |            -2.2 |       2.2 |
| EICHERMOT  | 7650    |     3.5 |      62 |      6.8 |     -7.9 |            -2.4 |       2.4 |
| ETERNAL    |  363.65 |     3.4 |      68 |     13.5 |     12.9 |            -2.3 |       2.7 |
| BHARTIARTL | 2106    |     3.4 |      70 |     16.6 |      5.4 |            -0.8 |       2.2 |
| SUNPHARMA  | 1880    |     3.3 |      65 |      6.2 |     -6.2 |            -3.3 |       2.3 |
| ICICIBANK  | 1583.6  |     3.2 |      76 |     16.4 |      7.7 |            -2   |       2   |
| INDIGO     | 5587.3  |     3.2 |      73 |     16.4 |      1.9 |            -2.2 |       2.6 |
| TITAN      | 4844.9  |     3.2 |      61 |      8   |     -7.9 |            -4.2 |       2.4 |
| JSWSTEEL   | 1348    |     3.1 |      65 |     14.6 |      3.3 |            -1.6 |       2.2 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| JIOFIN     |   227.5 |     1.5 |      59 |      4.5 |    -14   |
| SHRIRAMFIN |   970   |     1.3 |      57 |     -1   |    -15.4 |
| INFY       |  1141.5 |     1.1 |      56 |      9.9 |     -3.6 |
| TMPV       |   287.4 |     1   |      52 |      0.5 |    -19.1 |
| NESTLEIND  |  1263.2 |     1   |      49 |     -5.3 |    -19.1 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
