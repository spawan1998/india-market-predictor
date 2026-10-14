## NIFTY50 daily read: 2026-10-14

Close **22,622.70** (2026-10-14). Model P(up over next 5 sessions) = **0.625**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3654 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.09 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| KOTAKBANK  |  438.05 |     4.7 |      64 |      4.5 |     22   |            -1.6 |       2.1 |
| TECHM      | 1575.2  |     4.6 |      56 |      2.2 |     11.2 |            -0.9 |       2.8 |
| HCLTECH    | 1327    |     4.1 |      63 |     10   |     20.8 |            -2   |       3   |
| NESTLEIND  | 1383.2  |     3.7 |      55 |     -0   |      3.2 |            -1   |       2.3 |
| TCS        | 2304.9  |     3.6 |      65 |      5.3 |     11.9 |            -1.3 |       3   |
| TRENT      | 2971    |     3.5 |      63 |      6   |      9.6 |            -1.1 |       2.5 |
| ADANIPORTS | 1748.7  |     3.5 |      49 |     -0.9 |      1.7 |            -4.1 |       2.7 |
| INFY       | 1088    |     3.5 |      59 |      4.8 |      7.1 |            -0.8 |       2.7 |
| AXISBANK   | 1264.6  |     3.2 |      57 |      1.5 |      2.4 |            -0.9 |       2   |
| ITC        |  261.5  |     2.6 |      47 |      0.6 |      0.6 |            -3.5 |       2.4 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| RELIANCE   |  1174.6 |     0.1 |      39 |     -6.6 |     -3.3 |
| M&M        |  2793.7 |     0.1 |      31 |    -10.1 |     -3.3 |
| SUNPHARMA  |  1746.4 |     0   |      33 |     -5.1 |     -4.5 |
| ASIANPAINT |  2344.7 |     0   |      39 |     -5.2 |     -6.1 |
| SBILIFE    |  1650   |     0   |      37 |     -2.1 |     -5.5 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
