# Build two DataFrames indexed by ticker
prices = pd.DataFrame(
    {"price": [180, 380, 500]},
    index=["AAPL", "MSFT", "NVDA"]
)

fundamentals = pd.DataFrame(
    {"pe_ratio": [29, 35, 70], "market_cap": [2.9e12, 2.8e12, 1.2e12]},
    index=["AAPL", "MSFT", "NVDA"]
)

# Join on index — default is left join
combined = prices.join(fundamentals)
print(combined)
#       price  pe_ratio    market_cap
# AAPL    180        29  2.900000e+12
# MSFT    380        35  2.800000e+12
# NVDA    500        70  1.200000e+12
