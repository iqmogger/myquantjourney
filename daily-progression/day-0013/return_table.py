import yfinance as yf
import numpy as np

df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
close = df["Close"].squeeze()

# Step 1: Get monthly returns using resample (Concept 1)
monthly_returns = close.resample("ME").last().pct_change().dropna()

# Step 2: Extract year and month from the index
# We need these as separate columns to build the pivot table
years  = monthly_returns.index.year
months = monthly_returns.index.month

# Step 3: Build the pivot table
# .groupby([list_of_groupers]) groups by MULTIPLE things at once
# Then .unstack() pivots one level into columns
return_table = monthly_returns.groupby([years, months]).first().unstack()

# The result: rows = years, columns = month numbers (1–12)
# Let's rename the columns to month abbreviations
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
return_table.columns = month_names

# Format as percentages for display
print("Monthly Return Table (%):")
print((return_table * 100).round(2))
print()

# ── Add a YTD (year-to-date) column ──
# For each year, compound all monthly returns
# (1 + r1) * (1 + r2) * ... - 1
# That's what .prod() does after adding 1

return_table["YTD"] = (1 + return_table[month_names]).prod(axis=1) - 1
print("With YTD column:")
print((return_table * 100).round(2))
