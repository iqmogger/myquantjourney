import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT', 'TSLA', 'SPY'] # Multiple !

data = yf.download(tickers, start='2024-01-01', end='2025-01-01')
print(data.head()) # Only a couple row
print(data.shape)  # (rows, columns)]

# Just coses:
closes = data['Close']
print(closes.head())
# Now each column is one stock
