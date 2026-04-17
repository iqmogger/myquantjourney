import pandas as pd
import yfinance as yf

data = yf.download('AAPL', start='2024-01-01', end='2025-01-01', auto_adjust=True)
data.columns = data.columns.droplevel(1)  # droplevel basically gets rid of row 2. It counts from 0.

# Calculate a 20-day moving average (you know this from Day 0003)
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Now the new part — create a Series of True/False values
above_sma = data['Close'] > data['SMA_20']
print(above_sma.head(25))
