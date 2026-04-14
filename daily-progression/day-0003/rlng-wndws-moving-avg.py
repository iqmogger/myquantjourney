# A moving average is the average of the last N days of closing prices. It "smooths out" noise.

import pandas as pd
import yfinance as yf

# Download Apple stock for the last year
apple = yf.download('AAPL', start='2025-01-01', end='2026-01-01')

# The index is automatically dates (go look at apple.index)

# Simple Moving Average (SMA)
apple['SMA_20'] = apple['Close'].rolling(window=20).mean()
# Notation explained:
# apple['SMA_20'] is creating a new column
# .rolling(window=n) is basically like a sliding window that moves through the data one row at a time.
# What it does is it basicvally gives you the average return every n days. 

# This creates a NEW column where each value is the average of the last 20 closes
print(apple[['Close', 'SMA_20']].head(25))
# Head 25 is first 25 numbers.
