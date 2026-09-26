# Statistical Arbitrage Using Pairs Trading

A quantitative research project implementing a market-neutral pairs-trading strategy on NIFTY equities using cointegration, OLS hedge-ratio estimation, rolling spread Z-scores, and an out-of-sample backtest.

## Research objective
Test whether a statistically related pair can produce a mean-reversion signal after accounting for delayed execution and transaction costs.

## Strategy
For HDFCBANK and KOTAKBANK, estimate:

`log(P_A) = alpha + beta * log(P_B) + epsilon`

and define the spread:

`S_t = log(P_A,t) - beta * log(P_B,t)`

The strategy uses a 20-day rolling Z-score:

`Z_t = (S_t - mean_20(S)) / std_20(S)`

- `Z > +1.5`: short the spread
- `Z < -1.5`: long the spread
- return toward `|Z| < 0.5`: exit
- execution: next trading period
- transaction cost assumption: 5 bps per unit position change

## Validation design
The data is split chronologically:

- **Training:** 2018-01-01 to 2023-08-03
- **Test:** 2023-08-04 to 2024-12-31

The pair's cointegration and hedge ratio are estimated using training data. The final test period is then evaluated without changing the signal rules based on test performance.

The Z-score thresholds in this case study are fixed research parameters rather than optimized against the final test set. This is intentional: maximizing a test-period metric would introduce data snooping.

## Reference out-of-sample run
The included code produces the following reproducible reference run on the supplied dataset:

| Metric | Result |
|---|---:|
| Cointegration p-value | 0.0172 |
| ADF p-value | 0.00138 |
| Hedge ratio | 0.9788 |
| CAGR | **6.33%** |
| Annualized volatility | 7.08% |
| Sharpe | **0.931** |
| Sortino | **1.132** |
| Max drawdown | **-5.09%** |
| Final equity | **1.0904** |
| Position changes | 47 |

These are historical backtest statistics, not live-trading results or a claim of future profitability.

## Why this version is stronger
- avoids full-sample pair selection for the test period
- estimates the hedge ratio before the test period
- uses rolling statistics instead of full-sample Z-scores
- shifts the position by one period for execution
- charges transaction costs on position changes
- reports both return and risk metrics
- keeps the final test period separate from parameter selection

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Outputs:
- `outputs/tables/case_study_metrics.csv`
- `outputs/tables/case_study_timeseries.csv`
- `outputs/plots/equity_curve.png`
- `outputs/plots/z_score.png`

## Interview questions to prepare
1. Why cointegration instead of correlation?
2. What does the Engle-Granger p-value test?
3. Why estimate the hedge ratio with OLS?
4. Why use log prices?
5. Why does the spread need to be stationary?
6. What is look-ahead bias?
7. Why is next-period execution used?
8. How do transaction costs change the strategy?
9. What is survivorship bias in a stock universe?
10. Why might a static hedge ratio break down?
11. How would you make beta time-varying?
12. How would you perform walk-forward validation?
13. What would happen if the spread stopped mean-reverting?
14. How would you extend this from one pair to a portfolio?

## Project structure

```text
Statistical-Arbitrage-Using-Pairs-Trading/
├── data/raw/
│   └── nifty50_prices.csv
├── docs/
│   └── INTERVIEW.md
├── outputs/
│   ├── plots/
│   └── tables/
├── src/
│   └── run_case_study.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```
