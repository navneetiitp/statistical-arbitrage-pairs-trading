# Statistical Arbitrage Strategy Report

## Strategy Overview

This project implements a statistical arbitrage pairs trading strategy using NIFTY 50 stocks.

The strategy identifies cointegrated stock pairs and trades based on mean reversion in the spread between the assets.

## Methodology

1. Collect historical price data for NIFTY 50 stocks
2. Identify highly correlated pairs
3. Perform cointegration testing
4. Construct the spread using OLS hedge ratio
5. Generate trading signals using Z-score thresholds
6. Backtest the strategy across multiple pairs

## Key Results

- The strategy generated strong cumulative returns.
- Performance significantly outperformed the NIFTY benchmark.
- Rolling Sharpe ratio indicates stable risk-adjusted performance.
- Drawdowns remained moderate for a market-neutral strategy.

## Conclusion

The results demonstrate that cointegration-based pairs trading can successfully exploit short-term market inefficiencies while maintaining controlled risk.