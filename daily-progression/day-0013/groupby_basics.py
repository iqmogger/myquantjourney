import yfinance as yf
import numpy as np

df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
close = df["Close"].squeeze()
returns = close.pct_change().dropna()

# ── Grouping by a property of the index ──
# 
# Our index is dates. Every date has properties you can extract:
#   .index.year        — the year (2020, 2021, ...)
#   .index.month       — the month number (1–12)
#   .index.day_of_week — the weekday (0=Monday, 4=Friday)
#   .index.quarter     — the quarter (1, 2, 3, 4)

# GROUP BY YEAR — average daily return per year
yearly_avg = returns.groupby(returns.index.year).mean()
print("Average daily return by year:")
print(yearly_avg)
print()

# That's a tiny number (daily return). Let's annualize it:
# Multiply by 252 trading days to get approximate annual return
yearly_ann = returns.groupby(returns.index.year).mean() * 252
print("Annualized return by year (approx):")
print(yearly_ann)
print()

# GROUP BY MONTH — which month is best for AAPL?
monthly_avg = returns.groupby(returns.index.month).mean() * 21
# * 21 because ~21 trading days per month — gives rough monthly return
print("Average monthly return by calendar month:")
print(monthly_avg)
print()

# GROUP BY WEEKDAY — the "day of week effect"
# This is a real thing quants study: do stocks behave differently
# on Mondays vs Fridays?
day_names = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri"}
weekday_avg = returns.groupby(returns.index.day_of_week).mean()
print("Average daily return by weekday:")
for day_num, avg_ret in weekday_avg.items():
    print(f"  {day_names[day_num]}: {avg_ret:.6f}")
