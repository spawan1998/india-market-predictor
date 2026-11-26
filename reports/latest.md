## NIFTY50 daily read: 2026-11-26

Close **25,819.25** (2026-11-25). Model P(up over next 5 sessions) = **0.577**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.492, AUC 0.501, always-up baseline 0.569 over 3681 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.4% | -46.0% | -0.04 | 573 |
| sma200 | +4.3% | -28.6% | 0.44 | 123 |
| combo | -3.3% | -51.2% | -0.35 | 485 |
| buy_and_hold | +11.6% | -38.4% | 0.78 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| INDIGO     |  5720   |     4.4 |      69 |     25.7 |      5.5 |            -0.8 |       2.6 |
| CIPLA      |  1433.2 |     3.8 |      64 |      7.1 |     -6.4 |            -1   |       1.9 |
| DRREDDY    |  1398   |     3.7 |      68 |     13.7 |     12.5 |            -0.7 |       1.8 |
| TRENT      |  3319.6 |     3.7 |      70 |     21.7 |      7.1 |            -0.9 |       2.6 |
| ULTRACEMCO | 12800   |     3.7 |      69 |     15.8 |      4.2 |            -1.4 |       2.1 |
| HDFCLIFE   |   601.3 |     3.6 |      64 |     14.8 |      1.9 |            -1.4 |       2.9 |
| AXISBANK   |  1418.1 |     3.6 |      67 |     16.5 |      7.4 |            -2.8 |       2.5 |
| TCS        |  2517.3 |     3.6 |      63 |     -0.5 |      3.5 |            -1.9 |       2.8 |
| BAJAJ-AUTO | 10868   |     3.5 |      56 |      7.9 |    -13.6 |            -2.7 |       2.2 |
| EICHERMOT  |  8336   |     3.4 |      74 |     18   |     -2.4 |            -0.3 |       2.5 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HINDALCO  |  889.9  |     1.3 |      41 |      2.3 |    -20.4 |
| JIOFIN    |  222.85 |     1.1 |      51 |      8.7 |    -15.1 |
| NTPC      |  318    |     1.1 |      50 |      7.7 |    -11   |
| TATASTEEL |  159.3  |     1   |      29 |     -5   |    -19.4 |
| COALINDIA |  385    |     0.3 |      41 |     -0.6 |     -7.8 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
