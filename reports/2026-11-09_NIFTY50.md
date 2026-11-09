## NIFTY50 daily read: 2026-11-09

Close **25,030.35** (2026-11-06). Model P(up over next 5 sessions) = **0.606**: BULLISH lean (strong for this model).

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
| ADANIPORTS |  1942.7  |     4.7 |      68 |     13.7 |     13.1 |            -0.8 |       2.6 |
| JSWSTEEL   |  1347    |     4   |      65 |     14.6 |      2.1 |            -1.7 |       2.4 |
| BAJAJ-AUTO | 10979    |     4   |      63 |     13.9 |     -7.5 |             0   |       2.4 |
| TMCV       |   436.65 |     3.9 |      61 |      5.7 |     -5.2 |            -0.7 |       3.4 |
| ETERNAL    |   363.45 |     3.8 |      69 |     13.9 |     13.8 |            -0.6 |       2.7 |
| EICHERMOT  |  7629    |     3.8 |      62 |     12.7 |     -6.5 |            -1.1 |       2.2 |
| CIPLA      |  1403.8  |     3.8 |      64 |      7.4 |     -5.7 |            -1.2 |       1.9 |
| ICICIBANK  |  1589    |     3.7 |      81 |     17.8 |     10.2 |            -0.2 |       2   |
| BAJFINANCE |  1064.85 |     3.7 |      66 |     11.4 |     -2.8 |            -2.1 |       2.9 |
| APOLLOHOSP |  8549.5  |     3.7 |      60 |     11.5 |     -5.9 |            -1.7 |       2.5 |

## NIFTY 50 swing scan: weakest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:-----------|--------:|--------:|--------:|---------:|---------:|
| SBILIFE    |  1748   |     1.6 |      60 |      3.9 |     -7.4 |
| INFY       |  1154.1 |     1.4 |      58 |     18.4 |     -1.1 |
| MAXHEALTH  |   915   |     1.4 |      55 |      4.8 |    -16.1 |
| TATACONSUM |  1083.9 |     1.3 |      70 |     13.9 |     -1.5 |
| NESTLEIND  |  1297.8 |     1   |      56 |     -1.6 |    -17.3 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
