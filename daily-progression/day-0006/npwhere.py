import pandas as pd
import yfinance as yf

data = yf.download('AAPL', start='2024-01-01', end='2025-01-01', auto_adjust=True)
data.columns = data.columns.droplevel(1)  

# Calculate a 20-day moving average (you know this from Day 0003)
data['SMA_20'] = data['Close'].rolling(window=20).mean()

import numpy as np

# np.where(condition, value_if_True, value_if_False)
data['position'] = np.where(data['Close'] > data['SMA_20'], 1, 0)    # Just finds where exactly daily ret. is more that 20 day SMA. returns 1 or 0 (or -1). 
print(data['position'])
