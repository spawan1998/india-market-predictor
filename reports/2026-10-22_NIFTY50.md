## NIFTY50 daily read: 2026-10-22

Close **22,687.65** (2026-10-22). Model P(up over next 5 sessions) = **0.557**: mild bullish lean.

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.493, AUC 0.501, always-up baseline 0.568 over 3659 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is below the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -2.0% | -46.0% | -0.08 | 571 |
| sma200 | +4.0% | -28.6% | 0.42 | 122 |
| combo | -3.7% | -51.2% | -0.39 | 484 |
| buy_and_hold | +10.8% | -38.4% | 0.73 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |    close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|---------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| ICICIBANK  |  1398.5  |     4.2 |      59 |      4   |      3.3 |            -0.9 |       1.8 |
| TECHM      |  1829.1  |     3.8 |      76 |     17.4 |     22.7 |            -0.8 |       2.9 |
| HCLTECH    |  1421.7  |     3.7 |      74 |     12   |     21.4 |            -0.4 |       2.8 |
| INFY       |  1153.35 |     3.6 |      64 |     11.1 |     15.1 |            -1.8 |       2.8 |
| TCS        |  2506.9  |     3.6 |      74 |     18.4 |     19.6 |            -1   |       2.9 |
| BHARTIARTL |  1895    |     3.6 |      59 |      3.5 |      3.9 |            -1.8 |       2.2 |
| KOTAKBANK  |   437    |     3.3 |      58 |      5.4 |     20.1 |            -3.6 |       2.1 |
| WIPRO      |   190.41 |     3   |      74 |     15.7 |     15.9 |            -1.3 |       2.6 |
| DRREDDY    |  1239    |     3   |      58 |      3.4 |     10.2 |            -1.1 |       2.1 |
| ULTRACEMCO | 10958    |     2.8 |      52 |     -1.3 |     -0.5 |            -2.3 |       2.4 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| HINDUNILVR |  1828.3 |       0 |      38 |     -6.1 |     -9.7 |
| NTPC       |   302.6 |       0 |      30 |     -7.3 |     -7.3 |
| MAXHEALTH  |   817   |       0 |      21 |    -23.4 |    -19   |
| SHRIRAMFIN |   900.9 |       0 |      35 |    -11   |     -9.5 |
| TMPV       |   270   |       0 |      33 |    -10.5 |    -12.2 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
