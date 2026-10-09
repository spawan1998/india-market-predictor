## NIFTY50 daily read: 2026-10-09

Close **22,520.45** (2026-10-09). Model P(up over next 5 sessions) = **0.576**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.525, balanced 0.499, AUC 0.506, always-up baseline 0.567 over 3651 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.7% | -42.0% | -0.06 | 543 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.6% | -50.6% | -0.37 | 454 |
| buy_and_hold | +10.7% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| KOTAKBANK  |  441    |     4.8 |      68 |      5.2 |     24   |            -1   |       2.2 |
| TRENT      | 2918.2  |     4.5 |      61 |      4.5 |      7.5 |            -0.6 |       2.6 |
| ETERNAL    |  323.45 |     4   |      49 |      0.6 |     18.6 |            -6.1 |       2.8 |
| ADANIPORTS | 1761    |     3.7 |      51 |      3   |      3.3 |            -3.5 |       2.7 |
| ICICIBANK  | 1355    |     3.4 |      50 |     -3.2 |      4.5 |            -2.7 |       1.6 |
| AXISBANK   | 1259.1  |     3.2 |      56 |      1.1 |      2.1 |            -0.5 |       2.1 |
| ITC        |  266    |     2.9 |      50 |      0.9 |      1.4 |            -1.9 |       2.4 |
| TCS        | 2156    |     2.8 |      51 |     -4.4 |     11.7 |            -7.2 |       2.9 |
| TECHM      | 1514.1  |     2.6 |      43 |     -2.9 |     11   |            -7.3 |       2.6 |
| BHARTIARTL | 1805.1  |     2.4 |      47 |     -2.1 |      2.1 |            -4.7 |       1.9 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| POWERGRID  |  249.15 |       0 |      36 |     -6.2 |     -4.6 |
| TATACONSUM |  955    |       0 |      38 |     -5.8 |     -7.1 |
| TMPV       |  279.9  |       0 |      37 |     -8.7 |    -10.2 |
| ASIANPAINT | 2339.1  |       0 |      36 |     -5.7 |     -5.7 |
| HINDUNILVR | 1856.7  |       0 |      39 |     -6.2 |     -6.7 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
