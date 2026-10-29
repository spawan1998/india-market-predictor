## NIFTY50 daily read: 2026-10-29

Close **22,936.75** (2026-10-29). Model P(up over next 5 sessions) = **0.400**: BEARISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3664 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.09 | 572 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.74 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ETERNAL    |  337.85 |     4.9 |      59 |      2.1 |     13.8 |            -0.4 |       3.1 |
| BHARTIARTL | 1972.1  |     4   |      65 |     11.3 |      6.5 |            -0.3 |       2.3 |
| ADANIPORTS | 1872    |     4   |      65 |      7.4 |     14.3 |             0   |       2.7 |
| KOTAKBANK  |  459    |     3.9 |      68 |     14.3 |     23   |            -0.3 |       2.2 |
| DRREDDY    | 1345    |     3.7 |      75 |     10.2 |     23.2 |            -0.6 |       2.3 |
| JSWSTEEL   | 1255.4  |     3.6 |      54 |     -0.7 |      3.8 |            -1.6 |       2.6 |
| TATACONSUM | 1021    |     3.2 |      60 |      6.4 |     -1.4 |            -0.1 |       2.5 |
| TECHM      | 1769.6  |     3.1 |      66 |     15.7 |     13.9 |            -4.1 |       3   |
| LT         | 3837.1  |     3.1 |      59 |      1.9 |      3   |            -1.5 |       2.2 |
| SBIN       |  971.9  |     3.1 |      51 |      1   |      1.3 |            -1.2 |       1.9 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HDFCLIFE  |  517    |     0.2 |      39 |     -2.7 |     -1.7 |
| HDFCBANK  |  683.3  |     0.1 |      39 |     -5   |     -3.3 |
| TATASTEEL |  169.46 |     0   |      37 |     -9   |     -4.1 |
| NESTLEIND | 1188.6  |     0   |      33 |    -11.7 |    -15.5 |
| TMPV      |  266    |     0   |      34 |     -5.6 |    -13.9 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
