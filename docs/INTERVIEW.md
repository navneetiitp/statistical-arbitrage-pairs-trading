# Interview Preparation

### What did you build?
A market-neutral pairs-trading research pipeline. I selected a statistically related equity pair, estimated its hedge ratio, constructed a spread, generated mean-reversion signals from a rolling Z-score, and evaluated the strategy out of sample with delayed execution and transaction costs.

### Correlation vs cointegration
Correlation measures co-movement and can be high even for unrelated non-stationary series. Cointegration asks whether a linear combination of the series is stationary, which is closer to the requirement for a mean-reverting spread.

### Why OLS?
OLS provides a simple interpretable estimate of beta for the chosen regression specification. It is not the only possible hedge-ratio estimator; total-least-squares, minimum-variance and state-space approaches can also be considered.

### Why next-day execution?
The signal is computed using information available at time t. Shifting the position to t+1 avoids assuming that the strategy can trade at the same closing price that generated the signal.

### What are the main biases to discuss?
Look-ahead bias, survivorship bias, data-snooping/overfitting, stale prices, corporate-action issues, and unrealistic transaction-cost/slippage assumptions.

### Why can a good Sharpe still be misleading?
A backtest can look attractive because of parameter tuning, leakage, an unusually favorable sample period, or underestimated costs. Robustness across periods and parameter perturbations matters.

### How does Project 3 extend this?
A static beta assumes the relationship is stable. A Kalman filter can model beta as a latent state and update the hedge ratio sequentially as new observations arrive.
