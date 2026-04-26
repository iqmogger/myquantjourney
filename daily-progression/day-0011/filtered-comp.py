numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only keep even numbers
# NEW syntax: [WHAT for ITEM in LIST if CONDITION]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
# n % 2 == 0 means "n divided by 2 has remainder 0" — that's even
# The % operator is called "modulo" — it gives the remainder of division

# Only keep numbers greater than 5
big = [n for n in numbers if n > 5]
print(big)  # [6, 7, 8, 9, 10]

#==========================

import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "META", "NVDA", "TSLA", "JPM", "BAC", "XOM"]

# Download 1 year of data
data = yf.download(tickers, start="2025-01-01", end="2025-12-31")
closes = data["Close"]

# Calculate total return for each ticker
# .iloc[-1] = last row, .iloc[0] = first row
total_returns = (closes.iloc[-1] / closes.iloc[0]) - 1

# Filter: only tickers that went UP this year
# NEW — .items() lets you loop through a Series as (name, value) pairs
# This is like .items() on dictionaries from Day 8
winners = [ticker for ticker, ret in total_returns.items() if ret > 0]
losers  = [ticker for ticker, ret in total_returns.items() if ret < 0]

print(f"Winners: {winners}")
print(f"Losers:  {losers}")

# Get the actual return values for winners only
winner_returns = {ticker: ret for ticker, ret in total_returns.items() if ret > 0}
# ^ This is a DICTIONARY comprehension — same idea, but with {} and key: value
print(winner_returns)
