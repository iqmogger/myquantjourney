tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "META", "NVDA", "TSLA"]

# NEW — Slicing: grab a chunk of a list
# list[start:stop]  — gives you items from index 'start' up to (but NOT including) 'stop'
first_three = tickers[0:3]       # ["AAPL", "MSFT", "GOOG"]
last_two    = tickers[-2:]       # ["NVDA", "TSLA"]
middle      = tickers[2:5]       # ["GOOG", "AMZN", "META"]

print(f"First 3: {first_three}")
print(f"Last 2:  {last_two}")
print(f"Middle:  {middle}")

# NEW — len() gives you the length of a list
print(f"Total tickers: {len(tickers)}")  # 7

# NEW — 'in' checks if something is in a list
# Returns True or False (a boolean, like Day 2)
print("AAPL" in tickers)   # True
print("GME" in tickers)    # False

# NEW — .append() adds an item to the end
tickers.append("JPM")
print(tickers)  # now has 8 items

# NEW — .remove() removes a specific item
tickers.remove("TSLA")
print(tickers)  # TSLA is gone
