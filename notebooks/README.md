# Jupyter Notebooks

This folder contains the research notebooks used to develop the statistical arbitrage pairs trading strategy.

Each notebook represents a step in the quantitative research pipeline.

## Notebook Overview

**01_data_collection.ipynb**  
Download historical price data for NIFTY 50 stocks using yfinance.

**02_correlation_analysis.ipynb**  
Compute correlation matrix and identify highly correlated stock pairs.

**03_cointegration_test.ipynb**  
Perform cointegration tests to find statistically valid trading pairs.

**04_spread_zscore.ipynb**  
Construct the spread between cointegrated assets and compute the Z-score.

**05_backtesting.ipynb**  
Backtest the basic pairs trading strategy using Z-score signals.

**06_auto_pairs_selection.ipynb**  
Automatically identify cointegrated pairs from the universe of stocks.

**07_multi_pair_backtest.ipynb**  
Run backtests across multiple trading pairs.

**08_pair_performance.ipynb**  
Evaluate profitability and performance of individual pairs.

**09_strategy_analysis.ipynb**  
Analyze overall strategy performance including equity curve, Sharpe ratio, and drawdown.

**10_advanced_analysis.ipynb**  
Perform advanced diagnostics including half-life estimation and signal visualization.

## Notes

These notebooks represent the research and development workflow used to build the statistical arbitrage strategy.