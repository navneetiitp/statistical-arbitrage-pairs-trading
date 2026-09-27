# Statistical Arbitrage Using Pairs Trading

A quantitative research project implementing a market-neutral pairs-trading strategy on NIFTY equities using cointegration, OLS hedge-ratio estimation, rolling spread Z-scores, and an out-of-sample backtest.

## Research Objective

The objective is to test whether a statistically related equity pair can generate a mean-reversion trading signal after accounting for:

- chronological out-of-sample evaluation
- delayed execution
- transaction costs
- spread stationarity
- portfolio risk

The project focuses on **research methodology and causal backtesting**, rather than optimizing the strategy to produce an attractive historical result.

---

## Strategy

The case study uses **HDFCBANK and KOTAKBANK**.

The relationship is modeled as:

\[
\log(P_A) = \alpha + \beta\log(P_B) + \epsilon
\]

where:

- \(P_A\) = price of HDFCBANK
- \(P_B\) = price of KOTAKBANK
- \(\alpha\) = intercept
- \(\beta\) = OLS hedge ratio
- \(\epsilon\) = residual spread

The trading spread is defined as:

\[
S_t = \log(P_{A,t}) - \beta\log(P_{B,t})
\]

A 20-day rolling Z-score is then calculated:

\[
Z_t =
\frac{S_t-\operatorname{mean}_{20}(S)}
{\operatorname{std}_{20}(S)}
\]

### Trading Rules

- \(Z > +1.5\) → short the spread
- \(Z < -1.5\) → long the spread
- \(|Z| < 0.5\) → exit
- Execution → next trading period
- Transaction cost → 5 bps per unit position change

The strategy therefore trades deviations of the observed spread from its recent mean rather than taking a directional view on either stock individually.

---

## Validation Design

The dataset is divided chronologically:

| Period | Dates |
|---|---|
| Training | 2018-01-01 → 2023-08-03 |
| Test | 2023-08-04 → 2024-12-31 |

The pair's cointegration relationship and hedge ratio are estimated using the training period.

The final test period is then evaluated without changing the trading rules based on test-period performance.

The Z-score thresholds are fixed research parameters rather than optimized against the final test set. This avoids using the test period as a parameter-selection dataset.

### Research Pipeline

```text
Historical NIFTY Prices
        ↓
Training / Test Split
        ↓
Training-Only Pair Analysis
        ↓
Cointegration Test
        ↓
OLS Hedge-Ratio Estimation
        ↓
Spread Construction
        ↓
Rolling 20-Day Z-Score
        ↓
Trading Signal
        ↓
Next-Period Execution
        ↓
Transaction Costs
        ↓
Out-of-Sample P&L
        ↓
Risk & Performance Analysis
