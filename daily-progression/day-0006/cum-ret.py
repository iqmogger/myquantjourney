import pandas as pd
import yfinance as yf

data = yf.download('AAPL', start='2024-01-01', end='2025-01-01', auto_adjust=True)
data.columns = data.columns.droplevel(1)  

# Calculate a 20-day moving average (you know this from Day 0003)
data['SMA_20'] = data['Close'].rolling(window=20).mean()

import numpy as np

# np.where(condition, value_if_True, value_if_False)
data['position'] = np.where(data['Close'] > data['SMA_20'], 1, 0)  

# WRONG — this uses today's signal to "trade" today's return (impossible)
# data['strategy_return_wrong'] = data['position'] * data['Close'].pct_change()

# RIGHT — today's position was decided yesterday
data['strategy_return'] = data['position'].shift(1) * data['Close'].pct_change()

# Cumulative return = how much $1 would be worth
data['cumulative_strategy'] = (1 + data['strategy_return']).cumprod()
data['cumulative_buy_hold'] = (1 + data['Close'].pct_change()).cumprod()    # Basically these two last rows compare "buy + hold" and the strategy you're testing.
