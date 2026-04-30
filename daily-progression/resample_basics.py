import yfinance as yf
import matplotlib.pyplot as plt

# Download AAPL
df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")

# Daily close prices — you've seen this 100 times
close = df["Close"].squeeze()

# ── .resample() ──
# Syntax:  series.resample("frequency_code").aggregation_function()
#
# Frequency codes (memorize these):
#   "W"  = weekly
#   "ME" = month-end
#   "QE" = quarter-end
#   "YE" = year-end
#
# Aggregation functions (you already know these from Day 2):
#   .mean()   = average of the bucket
#   .sum()    = total
#   .last()   = last value in the bucket
#   .first()  = first value in the bucket
#   .std()    = standard deviation

# Monthly average closing price
monthly_avg = close.resample("ME").mean()
print("Monthly average close (first 5 months):")
print(monthly_avg.head())
print()

# Monthly LAST closing price — this is what you'd see on a monthly chart
monthly_close = close.resample("ME").last()
print("Monthly last close (first 5 months):")
print(monthly_close.head())
print()

# Weekly total volume
volume = df["Volume"].squeeze()
weekly_vol = volume.resample("W").sum()
print("Weekly total volume (first 5 weeks):")
print(weekly_vol.head())
print()

# ── WHY .mean() vs .last() matters ──
# If AAPL closes at $150, $155, $148, $160 during a month:
#   .mean()  = $153.25  (the average — smooths out noise)
#   .last()  = $160     (the final price — what your portfolio actually shows)
#   .first() = $150     (the opening price of the month)
# For calculating monthly RETURNS, you want .last()
# For smoothing out noise to see trends, you want .mean()

# ── Monthly returns using .last() ──
monthly_returns = monthly_close.pct_change().dropna()
print("Monthly returns (first 5):")
print(monthly_returns.head())
