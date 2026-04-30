# EXAMPLE 1: Simple transformation
# WITHOUT list comprehension:
prices = [100, 150, 200, 250, 300]
doubled = []
for price in prices:
    doubled.append(price * 2)
print(f"Doubled (loop): {doubled}")

# WITH list comprehension (same result, one line):
doubled = [price * 2 for price in prices]
print(f"Doubled (comp): {doubled}")

# EXAMPLE 2: Filtering (keep only items that pass a condition)
high_prices = [price for price in prices if price > 150]
print(f"Prices > $150: {high_prices}")

# EXAMPLE 3: Transform AND filter at the same time
doubled_high = [price * 2 for price in prices if price > 200]
print(f"Double prices > $200: {doubled_high}")

# FINANCE EXAMPLE: Daily returns
returns = [0.01, -0.02, 0.03, 0.015, -0.005, 0.002]

# Filter for positive return days
positive_days = [r for r in returns if r > 0]
print(f"\nReturns: {returns}")
print(f"Positive days: {positive_days}")

# Calculate what they would be if doubled
doubled_positive = [r * 2 for r in returns if r > 0]
print(f"Doubled positive: {doubled_positive}")

# Filter for loss days (negative)
loss_days = [r for r in returns if r < 0]
print(f"Loss days: {loss_days}")

# SYNTAX TEMPLATE:
# [NEW_VALUE for ITEM in LIST if CONDITION]
#  ^^^^^^^^^     ^^^^     ^^^^    ^^^^^^^^^
#  what to put   loop    iterate  optional
#  in new list   var     over     filter
