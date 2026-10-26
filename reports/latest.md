## NIFTY50 daily read: 2026-10-26

Close **22,753.20** (2026-10-26). Model P(up over next 5 sessions) = **0.435**: mild bearish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3661 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

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

| symbol     |    close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|---------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ICICIBANK  |  1403    |     4.3 |      59 |      4.7 |      3   |            -0.6 |       1.8 |
| ETERNAL    |   325.55 |     4.2 |      53 |     -5   |     20.5 |            -4.2 |       3.2 |
| BHARTIARTL |  1917.5  |     3.9 |      62 |      4.6 |      5.3 |            -0.6 |       2.3 |
| TECHM      |  1795    |     3.8 |      72 |     16.2 |     20.3 |            -2.7 |       3   |
| DRREDDY    |  1310.9  |     3.7 |      70 |      8.2 |     18.1 |            -0.6 |       2.4 |
| JSWSTEEL   |  1260    |     3.6 |      55 |     -2.9 |      5.8 |            -2.2 |       2.7 |
| INFY       |  1166    |     3.5 |      65 |     14.3 |     16.3 |            -2.7 |       3.7 |
| KOTAKBANK  |   440.75 |     3.5 |      59 |      6.7 |     18.8 |            -2.7 |       2.3 |
| ULTRACEMCO | 11180    |     3.2 |      57 |      0.2 |      0.6 |            -0.3 |       2.3 |
| ADANIPORTS |  1752.5  |     2.7 |      50 |     -3   |      3.4 |            -3.8 |       2.7 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| SBILIFE    |  1643.7 |       0 |      39 |     -6.6 |     -7.3 |
| TATACONSUM |   936.5 |       0 |      36 |     -5.8 |     -9.7 |
| SUNPHARMA  |  1740   |       0 |      36 |     -6.7 |     -6.1 |
| POWERGRID  |   247   |       0 |      36 |     -8.6 |     -9.6 |
| TMPV       |   263.7 |       0 |      29 |    -12.2 |    -14.3 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
