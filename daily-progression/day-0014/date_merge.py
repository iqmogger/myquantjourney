import pandas as pd
import yfinance as yf

# Pull two assets with potentially different trading days
spy = yf.download("SPY", start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"].squeeze()
tlt = yf.download("TLT", start="2023-01-01", end="2024-01-01", auto_adjust=True)["Close"].squeeze()

# Convert to DataFrames and reset index so Date is a column
spy_df = spy.reset_index()
spy_df.columns = ["date", "spy_price"]

tlt_df = tlt.reset_index()
tlt_df.columns = ["date", "tlt_price"]

# Merge on the date column
combined = spy_df.merge(tlt_df, on="date", how="inner")
print(combined.head())
print(f"Rows: {len(combined)}")
