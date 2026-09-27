# Statistical Arbitrage Using Pairs Trading

A reproducible quantitative research project implementing a **market-neutral pairs-trading strategy** on NIFTY equities using cointegration, OLS hedge-ratio estimation, rolling spread Z-scores, delayed execution, transaction costs, and an out-of-sample backtest.

The project focuses on building a statistically defensible research pipeline rather than optimizing historical performance.

---

## Research Objective

The objective is to investigate whether a statistically related pair of equities can generate a mean-reversion trading signal after accounting for:

- cointegration
- hedge-ratio estimation
- rolling spread statistics
- delayed execution
- transaction costs
- out-of-sample evaluation
- return and risk metrics

The case study uses **HDFCBANK and KOTAKBANK**.

The central research question is:

> **Can deviations from a historically stable relationship between two equities be converted into a systematic market-neutral trading strategy that remains meaningful out of sample?**

---

## Research Pipeline

```text
NIFTY Equity Prices
        │
        ▼
Chronological Train / Test Split
        │
        ▼
Training-Only Pair Analysis
        │
        ├── Cointegration Test
        │
        └── OLS Hedge-Ratio Estimation
        │
        ▼
Spread Construction
        │
        ▼
Rolling 20-Day Z-Score
        │
        ▼
Trading Signal
        │
        ▼
Next-Period Execution
        │
        ▼
Transaction Costs
        │
        ▼
Out-of-Sample P&L
        │
        ▼
Risk & Performance Analysis
