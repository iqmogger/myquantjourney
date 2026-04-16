import yfinance as yf
import pandas as pd
import numpy as np
 
tickers = ["AAPL", "AMZN", "GOOG", "META", "TSLA"]

data = yf.download(tickers, start='2023-01-01', end='2024-01-01')

closes = data['Close']
 
daily = closes.pct_change()

correlation = daily.corr()

print(correlation)

# then unstack
correlation_unstack = correlation.unstack()

print(correlation_unstack)

drop_duplicates = correlation_unstack.drop_duplicates()

print(drop_duplicates)

# So far I have a clean list with no duplicates. Now let's make it filtered.

filtered = drop_duplicates[drop_duplicates != 1.0]    # Its like "in d_d, d_d is NOT 1.0

highest = filtered.nlargest(1) # Find largest
lowest = filtered.nsmallest(1) # Find smallest

print(f"Highest: {highest.index[0]} = {highest.iloc[0]:.4f}")
print(f"Lowest: {lowest.index[0]} = {lowest.iloc[0]:.4f}")



weights = np.array([0.20, 0.20, 0.20, 0.20, 0.20])

portfolio_returns = daily.dot(weights)   # dot = matrix multiplication

volatility = daily.std()
dr_avg = daily.mean()
risk_free_rate = 0.04 / 252
sharpe = (dr_avg - risk_free_rate) / volatility


print(f" daily avg = {dr_avg}
volatility: {volatility}
Sharpe: {sharpe}")
