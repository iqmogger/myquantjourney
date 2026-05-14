# Build two DataFrames with overlapping but not identical keys
prices = pd.DataFrame({
    "ticker": ["AAPL", "MSFT", "NVDA", "AMZN"],
    "price": [180, 380, 500, 145]
})

fundamentals = pd.DataFrame({
    "ticker": ["AAPL", "MSFT", "NVDA", "GOOG"],
    "pe_ratio": [29, 35, 70, 25]
})

# Inner join — only tickers in BOTH
merged_inner = prices.merge(fundamentals, on="ticker", how="inner")
# Result: AAPL, MSFT, NVDA (AMZN and GOOG dropped)

# Left join — all tickers in prices, NaN where fundamentals missing
merged_left = prices.merge(fundamentals, on="ticker", how="left")
# Result: AAPL, MSFT, NVDA, AMZN (AMZN gets NaN for pe_ratio)

# Outer join — all tickers from either side
merged_outer = prices.merge(fundamentals, on="ticker", how="outer")
# Result: AAPL, MSFT, NVDA, AMZN, GOOG (NaNs where missing)
