# Old way (Day 8 for loop):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = []               # start with an empty list
for n in numbers:           # loop through each number
    squared.append(n ** 2)  # square it, add to the list
print(squared)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# NEW — List comprehension (same result, one line):
squared = [n ** 2 for n in numbers]
print(squared)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#====================

# More examples:

tickers = ["AAPL", "MSFT", "GOOG", "AMZN"]

# Make everything lowercase
lower = [t.lower() for t in tickers]
print(lower)  # ["aapl", "msft", "goog", "amzn"]
# .lower() is a string method — converts to lowercase

# Add a suffix
with_exchange = [t + ".US" for t in tickers]
print(with_exchange)  # ["AAPL.US", "MSFT.US", "GOOG.US", "AMZN.US"]

# Get the length of each ticker name
lengths = [len(t) for t in tickers]
print(lengths)  # [4, 4, 4, 4]
