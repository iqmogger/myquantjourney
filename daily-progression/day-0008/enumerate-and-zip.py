tickers = ["AAPL", "GOOGL", "MSFT"]

# enumerate() gives you a counter alongside each item
for i, ticker in tickers:      # ← This would CRASH — can't unpack a string into two variables
    pass

# Correct version:
for i, ticker in enumerate(tickers):
    print(f"{i}: {ticker}")
# 0: AAPL
# 1: GOOGL
# 2: MSFT


tickers = ["AAPL", "GOOGL", "MSFT"]
prices = [185.50, 142.30, 415.20]

# zip() walks through both lists in parallel
for ticker, price in zip(tickers, prices):
    print(f"{ticker}: ${price}")
# AAPL: $185.5
# GOOGL: $142.3
# MSFT: $415.2

