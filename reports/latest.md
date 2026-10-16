## NIFTY50 daily read: 2026-10-16

Close **23,146.15** (2026-10-16). Model P(up over next 5 sessions) = **0.588**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.567 over 3656 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.9% | -46.0% | -0.07 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.9% | -38.4% | 0.74 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ICICIBANK  |  1397   |     4.3 |      59 |      2.8 |      2.4 |            -0.1 |       1.8 |
| BHARTIARTL |  1905   |     4   |      62 |      3.8 |      5.9 |            -0.2 |       2.1 |
| TECHM      |  1790   |     3.9 |      76 |     14.9 |     18.7 |            -0.4 |       3   |
| AXISBANK   |  1290   |     3.8 |      63 |      3.9 |      2   |            -0.3 |       2   |
| KOTAKBANK  |   447.4 |     3.7 |      68 |      7.8 |     19.6 |            -1.3 |       2.1 |
| HCLTECH    |  1380   |     3.7 |      70 |     11.1 |     20.5 |            -0.3 |       2.9 |
| INFY       |  1161.2 |     3.7 |      70 |      9.5 |     10.8 |            -0.6 |       2.7 |
| TCS        |  2465   |     3.6 |      74 |     13.2 |     14.1 |            -0.8 |       3   |
| ADANIPORTS |  1750.8 |     3.5 |      50 |      1.6 |      0.2 |            -4   |       2.5 |
| TRENT      |  2958.7 |     3.4 |      62 |      6.8 |      9   |            -1.5 |       2.4 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| GRASIM     |  2920   |     0.2 |      38 |     -8.4 |     -0.9 |
| SUNPHARMA  |  1758.8 |     0   |      37 |     -5.1 |     -4.1 |
| ONGC       |   222   |     0   |      39 |     -6.3 |     -5   |
| APOLLOHOSP |  7890   |     0   |      37 |     -9.3 |     -5.6 |
| MAXHEALTH  |   846   |     0   |      25 |    -17.5 |    -17.5 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
