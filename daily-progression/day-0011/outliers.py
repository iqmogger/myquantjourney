import yfinance as yf
import numpy as np

df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
returns = df["Close"].pct_change().dropna()

mean = returns.mean()
std  = returns.std()

# A common rule: anything beyond 3 standard deviations is an "outlier"
# NEW — .abs() gives the absolute value (makes negatives positive)
outliers = returns[returns.abs() > 3 * std]
print(f"Found {len(outliers)} outlier days:")
print(outliers)

# These are days where the stock moved more than 3 standard deviations
# For AAPL, that's roughly a 5%+ daily move — rare but real

# To REMOVE outliers (careful — only do this if you think they're data errors):
clean_returns = returns[returns.abs() <= 3 * std]
print(f"\nBefore: {len(returns)} days")
print(f"After:  {len(clean_returns)} days")
print(f"Removed: {len(returns) - len(clean_returns)} days")

# NEW — .clip() caps values at a min and max
# Instead of removing outliers, you can "winsorize" them (cap at the boundary)
capped = returns.clip(lower=-3*std, upper=3*std)
# Any return below -3σ becomes exactly -3σ, above +3σ becomes +3σ
# This keeps the data point but limits its impact
