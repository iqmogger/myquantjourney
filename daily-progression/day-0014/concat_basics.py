import pandas as pd
import yfinance as yf

# Pull two non-overlapping time periods for the same ticker
spy_2022 = yf.download("SPY", start="2022-01-01", end="2023-01-01", auto_adjust=True)["Close"]
spy_2023 = yf.download("SPY", start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"]

# Stack them vertically (axis=0 is the default — stacking rows)
spy_combined = pd.concat([spy_2022, spy_2023], axis=0)
print(spy_combined.shape)  # ~504 rows (252 + 252)

# Now stack horizontally (axis=1 — side by side as columns)
spy = yf.download("SPY", start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"].squeeze()
qqq = yf.download("QQQ", start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"].squeeze()

prices = pd.concat([spy, qqq], axis=1)
prices.columns = ["SPY", "QQQ"]  # Name the columns
print(prices.head())
