## NIFTY50 daily read: 2026-10-21

Close **22,811.35** (2026-10-21). Model P(up over next 5 sessions) = **0.514**: NO EDGE - coin flip, stay out or size tiny.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.568 over 3658 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.9% | -46.0% | -0.08 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| TECHM      | 1834.7  |     4   |      77 |     19.4 |     22.1 |             0   |       2.9 |
| ICICIBANK  | 1385    |     3.9 |      56 |      3.4 |      1.2 |            -1.9 |       1.8 |
| INFY       | 1168    |     3.9 |      67 |     11.1 |     14.5 |            -0.2 |       2.8 |
| HCLTECH    | 1424.2  |     3.8 |      74 |     15   |     21.6 |             0   |       2.8 |
| BHARTIARTL | 1891.7  |     3.6 |      59 |     -0.1 |      4   |            -2   |       2.2 |
| TCS        | 2529    |     3.5 |      77 |     20.8 |     20.2 |            -0.2 |       2.9 |
| KOTAKBANK  |  437.8  |     3.3 |      58 |      6.1 |     19.1 |            -3.4 |       2.2 |
| WIPRO      |  189.17 |     3.2 |      73 |     13.4 |     15   |            -0.3 |       2.6 |
| DRREDDY    | 1244.5  |     3.1 |      60 |      5   |      8.9 |            -0.7 |       2   |
| RELIANCE   | 1209    |     2.5 |      48 |     -1.4 |     -1.6 |            -3.5 |       2.1 |

## NIFTY 50 swing scan: weakest

| symbol     |    close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|---------:|--------:|--------:|---------:|---------:|
| JIOFIN     |   211.39 |       0 |      35 |     -8   |     -6   |
| MAXHEALTH  |   819.9  |       0 |      21 |    -21.9 |    -19.8 |
| MARUTI     | 11200    |       0 |      33 |     -7.5 |    -11.1 |
| SHRIRAMFIN |   904.95 |       0 |      36 |    -10.4 |     -9.1 |
| TMPV       |   275.7  |       0 |      36 |     -9.2 |    -11.7 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
