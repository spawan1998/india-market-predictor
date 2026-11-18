## NIFTY50 daily read: 2026-11-18

Close **25,387.40** (2026-11-17). Model P(up over next 5 sessions) = **0.634**: BULLISH lean (strong for this model).

![price](./NIFTY50_price.png)

## How much to trust it

Walk-forward out-of-sample: accuracy 0.518, balanced 0.492, AUC 0.501, always-up baseline 0.569 over 3676 predictions. **No proven edge** (AUC ~0.5): treat the probability as noise. Close is above the 200-day SMA.

| strategy | CAGR | max DD | Sharpe | switches |
|---|---|---|---|---|
| ml | -1.5% | -46.0% | -0.05 | 573 |
| sma200 | +4.2% | -28.6% | 0.43 | 123 |
| combo | -3.5% | -51.2% | -0.36 | 485 |
| buy_and_hold | +11.5% | -38.4% | 0.78 | 1 |

Costs 20.0 bps per switch; ml enters above 0.55, exits below 0.50.

![equity](./NIFTY50_equity.png)

![importance](./NIFTY50_importance.png)

## NIFTY 50 swing scan: strongest

| symbol     |   close |   score |   rsi14 |   ret_1m |   rel_3m |   from_20d_high |   atr_pct |
|:-----------|--------:|--------:|--------:|---------:|---------:|----------------:|----------:|
| HDFCLIFE   |  595.05 |     3.6 |      68 |      8.1 |      6.9 |            -2.4 |       2.6 |
| AXISBANK   | 1369    |     3.4 |      71 |      6.3 |      8.3 |            -0.4 |       2.1 |
| INDIGO     | 5611    |     3.3 |      72 |     17.4 |      1.5 |            -1.8 |       2.5 |
| EICHERMOT  | 7828    |     3.2 |      66 |      8.3 |     -7.1 |            -1.5 |       2.6 |
| ETERNAL    |  375.05 |     3.1 |      73 |     16.1 |     13.6 |            -0.8 |       2.6 |
| ADANIPORTS | 1917    |     3.1 |      61 |     10   |      8.6 |            -3.1 |       2.5 |
| KOTAKBANK  |  497.25 |     2.9 |      77 |     11   |     22.9 |            -0.5 |       2   |
| SBILIFE    | 1815    |     2.9 |      64 |      9.2 |     -3.1 |            -1.1 |       2.4 |
| ITC        |  293.3  |     2.9 |      70 |     11.1 |      1.2 |            -1.2 |       2.3 |
| TRENT      | 3176.3  |     2.8 |      65 |      7.7 |      2.5 |            -2.6 |       2.6 |

## NIFTY 50 swing scan: weakest

| symbol    |   close |   score |   rsi14 |   ret_1m |   rel_3m |
|:----------|--------:|--------:|--------:|---------:|---------:|
| POWERGRID |   258   |     1.3 |      52 |      4.5 |     -6.1 |
| NTPC      |   321.8 |     1.3 |      56 |      3.3 |     -7.6 |
| INFY      |  1130   |     1   |      53 |      4.1 |     -5.3 |
| TATASTEEL |   181.5 |     1   |      52 |      2.9 |     -5.3 |
| TMPV      |   259.2 |     1   |      35 |     -9.7 |    -26.7 |

## Disclaimer

Educational tool. Out-of-sample accuracy on daily direction is typically 52-56%. A probability is a lean, not a forecast. Risk only what the position-size rule allows.
