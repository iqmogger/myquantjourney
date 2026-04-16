import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'TSLA', 'SPY']

data = yf.download(tickers, start='2024-01-01', end='2025-01-01')

import numpy as np

# Equal weights: 25% each across 4 stocks
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Portfolio daily return = sum of (weight × stock return) for each day
portfolio_returns = returns.dot(weights)
# .dot() = dot product = matrix multiplication (we'll explain this more later)

print(portfolio_returns.head())
