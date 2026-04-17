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

# shift(1) is important because it slides every value down one row. So the value that was on row 50 moves to row 51. Applied to positions, it means: "the position I hold today is the one I decided at yesterday's close

# this is important for backtesting. if you don't do it, then your sharpe ratio will be 5+ because of bias like it's gonna look ahead and use info that wouldn't available at the time of the trade

