import pandas as pd
import yfinance as yf

# Download Apple stock for the last year
apple = yf.download('AAPL', start='2025-01-01', end='2026-01-01')

# Calculate daily returns (did this yesterday)
apple['Daily_Return'] = apple['Close'].pct_change()

# Volatility = standard deviation of returns
volatility = apple['Daily_Return'].std()      #std is standard dev.
print(f"Daily volatility: {volatility:.4f}")     # About 0.015 = 1.5% per day
# .4f is how many decimal points it shows. Here it's 4.

# Annualized volatility (multiply by sqrt(252) trading days)
annual_volatility = volatility * (252 ** 0.5)
print(f"Annual volatility: {annual_volatility:.4f}")  # About 24% per year
