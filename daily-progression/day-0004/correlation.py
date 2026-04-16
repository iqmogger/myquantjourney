import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'TSLA', 'SPY']

data = yf.download(tickers, start='2024-01-01', end='2025-01-01')

closes = data['Close']

returns = closes.pct_change()
print(returns.head())
# Every column calculated at the same time

corr_matrix = returns.corr() # Simple notation. Just 
print(corr_matrix)

