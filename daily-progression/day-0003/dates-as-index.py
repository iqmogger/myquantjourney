import pandas as pd
import yfinance as yf

# Download Apple stock for the last year
apple = yf.download('AAPL', start='2025-01-01', end='2026-01-01')

# The index is automatically dates (go look at apple.index)
print(apple.index)  # DatetimeIndex

# Slice by date range
jan_data = apple['2025-01']  # All of January 2025
print(jan_data)

#Pretty straightforward
