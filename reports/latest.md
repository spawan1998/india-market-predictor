## NIFTY50 daily read: 2026-11-25

Close **25,349.65** (2026-11-23). Model P(up over next 5 sessions) = **0.671**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.519, balanced 0.492, AUC 0.501, always-up baseline 0.569 over 3680 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.5% | -46.0% | -0.05 | 573 |
| sma200 | +4.2% | -28.6% | 0.43 | 123 |
| combo | -3.5% | -51.2% | -0.36 | 485 |
| buy_and_hold | +11.5% | -38.4% | 0.77 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| CIPLA      | 1399.9  |     3.5 |      55 |      5.2 |     -7.3 |            -2.4 |       1.9 |
| DRREDDY    | 1380.1  |     3.5 |      64 |     11.4 |     12.3 |            -1.8 |       1.8 |
| APOLLOHOSP | 9257    |     3.3 |      71 |     21.7 |      1.4 |            -1.6 |       2.4 |
| KOTAKBANK  |  502.85 |     3.3 |      69 |     15.1 |     21.9 |            -3.6 |       2.3 |
| HCLTECH    | 1364.3  |     3.2 |      50 |     -4   |     -0.2 |            -7.1 |       2.7 |
| ITC        |  301    |     3.2 |      73 |     16.3 |      6.2 |            -0.8 |       2.2 |
| HDFCBANK   |  817.8  |     3.2 |      65 |     17.8 |      8.2 |            -4.9 |       2.4 |
| EICHERMOT  | 8172.5  |     3.2 |      71 |     15.4 |     -3   |            -1.2 |       2.6 |
| BAJAJFINSV | 1880.1  |     3.1 |      62 |     12   |    -11.4 |            -1.9 |       2.3 |
| AXISBANK   | 1388.6  |     3.1 |      64 |     14.6 |      6.4 |            -4.8 |       2.5 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| COALINDIA |  382    |       1 |      38 |     -2.7 |     -6   |
| NTPC      |  315.45 |       1 |      48 |      5.2 |     -9.2 |
| JIOFIN    |  219.7  |       1 |      47 |      4.2 |    -14.8 |
| TATASTEEL |  163    |       1 |      32 |     -5.4 |    -15.8 |
| TMPV      |  259    |       1 |      39 |     -4.1 |    -23.7 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
