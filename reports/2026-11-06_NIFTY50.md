## NIFTY50 daily read: 2026-11-06

Close **25,030.35** (2026-11-06). Model P(up over next 5 sessions) = **0.643**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.500, always-up baseline 0.568 over 3670 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.6% | -46.0% | -0.05 | 573 |
| sma200 | +4.1% | -28.6% | 0.43 | 123 |
| combo | -3.6% | -51.2% | -0.37 | 485 |
| buy_and_hold | +11.5% | -38.4% | 0.77 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |    close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|---------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| JSWSTEEL   |  1357.1  |     4.2 |      68 |     10.3 |      2.2 |            -0.9 |       2.4 |
| GRASIM     |  3227    |     4.2 |      70 |     10.5 |     -1.1 |            -0.2 |       2.1 |
| CIPLA      |  1411    |     4   |      67 |      6.3 |     -6.1 |             0   |       1.9 |
| ETERNAL    |   363.15 |     3.9 |      69 |     10.7 |     13.2 |             0   |       2.8 |
| SUNPHARMA  |  1860    |     3.9 |      67 |      4.4 |     -6.3 |            -0.5 |       2.3 |
| EICHERMOT  |  7669.5  |     3.9 |      64 |     10.2 |     -5.3 |            -0.6 |       2.3 |
| ADANIPORTS |  1936.6  |     3.8 |      68 |     10.7 |     12.7 |            -0.6 |       2.7 |
| ICICIBANK  |  1571.2  |     3.6 |      80 |     15.7 |      6.2 |             0   |       2.1 |
| BAJAJFINSV |  1864.7  |     3.5 |      69 |      7   |    -12.2 |             0   |       2.4 |
| BAJAJ-AUTO | 10900    |     3.4 |      61 |     10.3 |     -7.8 |            -0.3 |       2.4 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| SBILIFE    |  1784   |     2   |      68 |      3.4 |     -5.8 |
| TCS        |  2498.5 |     2   |      63 |     20.7 |      4.2 |
| HINDUNILVR |  1998.4 |     1.8 |      68 |      7.1 |     -5.5 |
| TATACONSUM |  1086.3 |     1.5 |      71 |     12.2 |     -1.9 |
| NESTLEIND  |  1282.1 |     1   |      53 |     -3.2 |    -18.1 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
