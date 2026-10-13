## NIFTY50 daily read: 2026-10-13

Close **22,721.95** (2026-10-13). Model P(up over next 5 sessions) = **0.597**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.493, AUC 0.500, always-up baseline 0.567 over 3653 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.08 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| KOTAKBANK  |   439   |     4.7 |      66 |      6   |     19.9 |            -1.4 |       2.2 |
| TRENT      |  2987.8 |     4.7 |      65 |      6   |      8.6 |            -0.1 |       2.5 |
| HCLTECH    |  1326   |     4.5 |      62 |      7.8 |     15.2 |             0   |       3.1 |
| ADANIPORTS |  1763   |     3.7 |      51 |     -0.7 |      2.9 |            -3.3 |       2.7 |
| ICICIBANK  |  1360.2 |     3.5 |      51 |     -2.1 |      2.8 |            -2.1 |       1.7 |
| TCS        |  2269.3 |     3.3 |      62 |      2.8 |     10.1 |            -2.3 |       2.9 |
| AXISBANK   |  1268.4 |     3.2 |      58 |      2.4 |      1.7 |            -0.5 |       2.1 |
| TECHM      |  1543.5 |     3.2 |      50 |      2.4 |      8.1 |            -5.5 |       2.6 |
| DRREDDY    |  1240   |     2.8 |      61 |      8.3 |      6   |            -1   |       2.3 |
| INFY       |  1062.1 |     2.7 |      54 |      2.6 |      1.9 |            -3.2 |       2.7 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| GRASIM     | 2912    |     0.2 |      31 |    -11.8 |     -1.6 |
| SUNPHARMA  | 1770.7  |     0.1 |      36 |     -5.1 |     -2.3 |
| ONGC       |  222.65 |     0   |      37 |     -4.9 |     -4.5 |
| TATACONSUM |  960    |     0   |      40 |     -4.1 |     -7.1 |
| POWERGRID  |  250.5  |     0   |      37 |     -5.8 |     -6.5 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
