## NIFTY50 daily read: 2026-11-20

Close **25,514.30** (2026-11-19). Model P(up over next 5 sessions) = **0.590**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.501, always-up baseline 0.569 over 3678 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.5% | -46.0% | -0.04 | 573 |
| sma200 | +4.2% | -28.6% | 0.44 | 123 |
| combo | -3.4% | -51.2% | -0.36 | 485 |
| buy_and_hold | +11.6% | -38.4% | 0.78 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| CIPLA      | 1418.5  |     3.8 |      63 |      7.1 |     -6.5 |            -1.1 |       1.8 |
| EICHERMOT  | 8058.5  |     3.5 |      69 |      9.7 |     -5.1 |            -0.2 |       2.7 |
| ITC        |  301    |     3.3 |      75 |     15.4 |      5.9 |            -0.3 |       2.2 |
| TRENT      | 3225    |     3.2 |      68 |     11.5 |      4   |            -1.1 |       2.5 |
| GRASIM     | 3111.1  |     3.2 |      55 |      8.1 |    -10.7 |            -3.9 |       2.3 |
| ETERNAL    |  366.85 |     3.2 |      64 |     14.6 |     10.5 |            -2.9 |       2.7 |
| DRREDDY    | 1400.9  |     3.1 |      74 |     12.7 |     13.2 |            -0.4 |       1.9 |
| ADANIPORTS | 1917.1  |     3   |      60 |      8.6 |      8.3 |            -3.1 |       2.4 |
| KOTAKBANK  |  503    |     3   |      77 |     13.7 |     24.1 |            -0   |       2   |
| SBIN       | 1156    |     2.9 |      81 |     18.7 |      4.2 |            -0.4 |       2.1 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HINDALCO  |  910    |     1.3 |      45 |      1.1 |    -18.3 |
| TATASTEEL |  180.89 |     1   |      52 |      3.9 |     -8.1 |
| WIPRO     |  183.93 |     0.4 |      45 |      1   |     -2.3 |
| TCS       | 2342.7  |     0.4 |      42 |     -4.8 |     -2.3 |
| INFY      | 1091.9  |     0.3 |      45 |     -1.2 |     -5.5 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
