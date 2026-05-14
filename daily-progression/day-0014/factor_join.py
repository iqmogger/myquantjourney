import pandas as pd
import yfinance as yf

tickers = ["AAPL", "MSFT", "NVDA", "GOOG", "AMZN"]

# Pull prices into a dict (the Day 4 pattern)
data = {}
for t in tickers:
    data[t] = yf.download(t, start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"].squeeze()

# Now combine into a single DataFrame with concat
prices = pd.concat(data, axis=1)
print(prices.head())
# Columns are now AAPL, MSFT, NVDA, GOOG, AMZN — all aligned by date
# NaN appears anywhere a ticker is missing a date (e.g., new IPO)

# Compute returns for all 5 at once
returns = prices.pct_change().dropna()

# Correlation matrix in one line
print(returns.corr())
