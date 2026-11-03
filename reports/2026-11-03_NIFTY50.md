## NIFTY50 daily read: 2026-11-03

Close **23,810.85** (2026-11-03). Model P(up over next 5 sessions) = **0.725**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.501, always-up baseline 0.567 over 3667 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

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
| ADANIPORTS | 1866.9  |     4.8 |      63 |      7.4 |     13.6 |            -0.4 |       2.6 |
| JSWSTEEL   | 1320    |     4.5 |      63 |      7.1 |      6   |            -0.2 |       2.5 |
| TRENT      | 3036.5  |     4.2 |      62 |     17.7 |      3.4 |            -0.9 |       2.8 |
| CIPLA      | 1396.9  |     4.2 |      64 |      3.9 |     -1.4 |             0   |       2   |
| ETERNAL    |  349.45 |     4   |      65 |     11.3 |     16.4 |            -0.2 |       2.8 |
| KOTAKBANK  |  464.65 |     3.9 |      69 |     11.1 |     20.8 |            -0.3 |       2.1 |
| LT         | 3948.2  |     3.8 |      66 |      6.9 |      2   |            -0.4 |       2   |
| INDIGO     | 5025    |     3.7 |      62 |      1.9 |     -3.1 |            -1.9 |       2.6 |
| GRASIM     | 3090    |     3.5 |      61 |      4.3 |     -1   |            -0.9 |       2.1 |
| RELIANCE   | 1307.9  |     3.4 |      67 |     12   |      3   |             0   |       2.6 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| HDFCLIFE  |   525.5 |     1.2 |      45 |     -1.6 |     -1.1 |
| SBILIFE   |  1683   |     1.2 |      51 |     -2.2 |     -8.2 |
| TMPV      |   276.7 |     1.1 |      47 |     -1   |    -16.9 |
| NESTLEIND |  1248.4 |     1   |      47 |     -4.5 |    -14.5 |
| ADANIENT  |  2593.3 |     0.3 |      43 |     -7.9 |    -11.6 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
