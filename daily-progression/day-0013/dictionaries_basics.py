import yfinance as yf

# CREATE a dictionary (like a phone book: name → number)
portfolio = {
    "AAPL": 150.00,
    "MSFT": 380.00,
    "GOOGL": 140.00
}
print(f"Portfolio: {portfolio}")

# ACCESS a value by key
apple_price = portfolio["AAPL"]
print(f"Apple price: ${apple_price}")

# ADD a new key-value pair
portfolio["TSLA"] = 250.00
print(f"After adding Tesla: {portfolio}")

# UPDATE an existing value
portfolio["AAPL"] = 155.00
print(f"After updating Apple: {portfolio}")

# CHECK if a key exists
if "MSFT" in portfolio:
    print("Microsoft is in the portfolio")

if "NVDA" in portfolio:
    print("NVIDIA in portfolio")
else:
    print("NVIDIA not in portfolio")

# GET all keys (symbols)
symbols = list(portfolio.keys())
print(f"\nAll symbols: {symbols}")

# GET all values (prices)
prices = list(portfolio.values())
print(f"All prices: {prices}")

# LOOP through a dictionary
print("\nAll holdings:")
for symbol, price in portfolio.items():
    print(f"  {symbol}: ${price}")

# MORE COMPLEX EXAMPLE: Portfolio with quantities
# Each value is now a dictionary itself (nested)
detailed_portfolio = {
    "AAPL": {"shares": 10, "price": 150.00},
    "MSFT": {"shares": 5, "price": 380.00},
    "GOOGL": {"shares": 2, "price": 140.00}
}

print(f"\nDetailed portfolio:\n{detailed_portfolio}")

# Access nested values
apple_shares = detailed_portfolio["AAPL"]["shares"]
apple_value = detailed_portfolio["AAPL"]["shares"] * detailed_portfolio["AAPL"]["price"]
print(f"Apple holdings: {apple_shares} shares = ${apple_value:.2f}")

# LOOP through and calculate totals
print("\nPosition totals:")
for symbol, info in detailed_portfolio.items():
    total = info["shares"] * info["price"]
    print(f"  {symbol}: {info['shares']} × ${info['price']} = ${total:.2f}")
