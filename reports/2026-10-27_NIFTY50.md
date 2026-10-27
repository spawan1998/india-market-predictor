## NIFTY50 daily read: 2026-10-27

Close **22,749.75** (2026-10-27). Model P(up over next 5 sessions) = **0.369**: BEARISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3662 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.09 | 572 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ETERNAL    |  331    |     4.8 |      56 |     -1.3 |     17.1 |            -1.2 |       3.1 |
| BHARTIARTL | 1978.8  |     4.2 |      69 |     10.2 |      9.1 |             0   |       2.3 |
| ICICIBANK  | 1386.9  |     4   |      54 |      3.9 |      1.9 |            -1.8 |       1.8 |
| JSWSTEEL   | 1252.7  |     3.6 |      54 |     -1.6 |      5.8 |            -2   |       2.8 |
| DRREDDY    | 1310    |     3.6 |      70 |      9.1 |     19   |            -1   |       2.4 |
| KOTAKBANK  |  442.5  |     3.5 |      60 |      9.3 |     20.2 |            -2.3 |       2.2 |
| INFY       | 1163    |     3.3 |      65 |     14.6 |     13   |            -2.9 |       3.6 |
| TECHM      | 1811.4  |     2.9 |      73 |     18.4 |     21.2 |            -1.8 |       2.9 |
| ONGC       |  229.85 |     2.8 |      54 |     -3.8 |      2   |            -2.5 |       1.7 |
| TATACONSUM | 1000    |     2.8 |      56 |      1.4 |     -4.5 |            -1.1 |       2.4 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| JIOFIN     |  207.24 |       0 |      33 |     -8.8 |     -6.9 |
| INDIGO     | 4596.5  |       0 |      36 |     -6   |     -6.9 |
| HINDUNILVR | 1818    |       0 |      37 |     -6   |    -11.2 |
| SBILIFE    | 1633    |       0 |      37 |     -7   |     -7.3 |
| TMPV       |  261.2  |       0 |      28 |    -11.5 |    -15.1 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
