import yfinance as yf
import pandas as pd
import numpy as np

df = yf.download("AAPL", start="2023-01-01", end="2025-01-01")
returns = df["Close"].pct_change()

# How many NaN values?
print(f"NaN count: {returns.isna().sum()}")
# .isna() returns True/False for each row (True if NaN)
# .sum() counts the Trues (True = 1, False = 0 in Python)

# Option 1: Drop NaN rows
clean = returns.dropna()
print(f"Before: {len(returns)} rows, After: {len(clean)} rows")
# You've used .dropna() before — now you know exactly what it does

# Option 2: Fill NaN with a value
filled = returns.fillna(0)
# .fillna(0) replaces every NaN with 0
# This makes sense for returns: "no data = no change"

# Option 3: Forward fill — use the previous day's value
filled_forward = returns.fillna(method="ffill")
# "ffill" = forward fill: if today is NaN, copy yesterday's value
# Useful for prices (a stock's price doesn't disappear, it stays the same)
# Less useful for returns (a missing return is NOT the same as yesterday's return)
