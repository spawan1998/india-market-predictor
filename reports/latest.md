## NIFTY50 daily read: 2026-10-15

Close **22,997.35** (2026-10-15). Model P(up over next 5 sessions) = **0.589**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3655 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.9% | -46.0% | -0.08 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.9% | -38.4% | 0.74 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| KOTAKBANK  |  447.95 |     5   |      69 |      9.3 |     23.4 |             0   |       2.1 |
| TECHM      | 1650    |     4.9 |      65 |      4.7 |     13.7 |             0   |       2.8 |
| HCLTECH    | 1360    |     4.3 |      67 |      8.5 |     20.2 |            -1.2 |       2.9 |
| AXISBANK   | 1288    |     3.8 |      62 |      5.3 |      3   |            -0.4 |       2   |
| TCS        | 2350    |     3.5 |      68 |      5   |     11.8 |            -1.5 |       3   |
| ICICIBANK  | 1389.4  |     3.4 |      58 |      2.9 |      3.3 |             0   |       1.8 |
| ADANIPORTS | 1743.2  |     3.4 |      49 |      1.7 |     -0.1 |            -4.4 |       2.6 |
| INFY       | 1110    |     3.3 |      63 |      3.1 |      7   |            -1.5 |       2.7 |
| TRENT      | 2949.7  |     3.3 |      61 |      8   |      7.6 |            -1.8 |       2.5 |
| ITC        |  263.9  |     2.7 |      50 |      2.3 |     -1.1 |            -2.6 |       2.3 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| HINDALCO   |  893.85 |     0.1 |      36 |     -6.8 |     -2.4 |
| M&M        | 2861.7  |     0.1 |      40 |     -5.5 |     -3.7 |
| SBILIFE    | 1661.8  |     0   |      40 |      0.5 |     -4.3 |
| ASIANPAINT | 2350    |     0   |      40 |     -2.2 |     -7.7 |
| SUNPHARMA  | 1764    |     0   |      38 |     -3.9 |     -5.1 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
