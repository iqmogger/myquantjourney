# This loop runs 3 times — once for each ticker in the list
# Each time, the variable 'ticker' takes on the next value

tickers = ["AAPL", "GOOGL", "MSFT"]

for ticker in tickers:
    print(f"Processing {ticker}...")

stock_prices = {"AAPL": 185.50, "GOOGL": 142.30, "MSFT": 415.20}

# Loop through keys only
for ticker in stock_prices:
    print(ticker)              # AAPL, GOOGL, MSFT

# Loop through keys AND values using .items()
for ticker, price in stock_prices.items():
    print(f"{ticker}: ${price}")
# AAPL: $185.5
# GOOGL: $142.3
# MSFT: $415.2

# Start with an empty dictionary
results = {}

tickers = ["AAPL", "GOOGL", "MSFT"]

for ticker in tickers:
    # For each ticker, store some calculated value
    results[ticker] = len(ticker)   # just an example — stores the string length

print(results)   # {"AAPL": 4, "GOOGL": 5, "MSFT": 4}


tickers = ["AAPL", "GOOGL", "MSFT"]

# enumerate() gives you a counter alongside each item
for i, ticker in tickers:      # ← This would CRASH — can't unpack a string into two variables
    pass

