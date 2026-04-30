import yfinance as yf
import numpy as np

df = yf.download("AAPL", start="2020-01-01", end="2025-01-01")
close = df["Close"].squeeze()
returns = close.pct_change().dropna()

# ── .agg() — multiple stats at once ──
# Instead of calling .mean(), .std(), .min() separately,
# pass a list of function names to .agg()

yearly_stats = returns.groupby(returns.index.year).agg(["mean", "std", "min", "max", "count"])

# This returns a DataFrame, not a Series — because you asked for multiple columns
print("Yearly return statistics:")
print(yearly_stats)
print()

# ── Renaming columns for clarity ──
yearly_stats.columns = ["Avg_Daily", "Volatility", "Worst_Day", "Best_Day", "Trading_Days"]
print("Renamed:")
print(yearly_stats)
print()

# ── Custom aggregation with a function you wrote ──
# Remember Day 5 — you can write your own functions
# Let's compute annualized Sharpe per year (Day 3 concept)

def sharpe(r):
    """Annualized Sharpe ratio from a Series of daily returns."""
    if r.std() == 0:
        return 0.0
    return (r.mean() / r.std()) * np.sqrt(252)

yearly_sharpe = returns.groupby(returns.index.year).apply(sharpe)
print("Sharpe ratio by year:")
print(yearly_sharpe)
