# Creating a dictionary
# The curly braces {} define a dictionary
# Each entry is   key: value   separated by commas

stock_prices = {"AAPL": 185.50, "GOOGL": 142.30, "MSFT": 415.20}

# Use square brackets with the key name to get the value
print(stock_prices["AAPL"])    # 185.50
print(stock_prices["GOOGL"])   # 142.30

# Add a new key-value pair — just assign to a new key
stock_prices["TSLA"] = 248.00

# Change an existing value — same syntax, just use an existing key
stock_prices["AAPL"] = 190.00

print(stock_prices)
# {"AAPL": 190.00, "GOOGL": 142.30, "MSFT": 415.20, "TSLA": 248.00}

# The 'in' keyword checks if a key is in the dictionary
# It returns True or False

print("AAPL" in stock_prices)   # True
print("AMZN" in stock_prices)   # False

# .keys() gives you all the keys
print(stock_prices.keys())    # dict_keys(["AAPL", "GOOGL", "MSFT", "TSLA"])

# .values() gives you all the values
print(stock_prices.values())  # dict_values([190.0, 142.3, 415.2, 248.0])

# .items() gives you both as pairs — you'll use this with loops
print(stock_prices.items())   # dict_items([("AAPL", 190.0), ("GOOGL", 142.3), ...])

metrics = {
    "sharpe": 1.45,
    "max_drawdown": -0.18,
    "cagr": 0.12
}


# CODE BY CLAUDE.
