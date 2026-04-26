import yfinance as yf
import pandas as pd
import numpy as np

def clean_pipeline(ticker, start, end):
    """Download data, clean it, and return ready-to-use returns.
    """
    
    # Step 1: Download
    try:
        df = yf.download(ticker, start=start, end=end)
        if len(df) == 0:
            print(f"WARNING: No data for {ticker}")
            return None
    except Exception as e:
        print(f"ERROR downloading {ticker}: {e}")
        return None
    
    # Step 2: Calculate returns
    returns = df["Close"].pct_change()
    
    # Step 3: Count and report missing values
    nan_count = returns.isna().sum()
    if nan_count > 1:  # 1 NaN is expected from pct_change()
        print(f"WARNING: {ticker} has {nan_count} missing values")
    
    # Step 4: Drop NaN
    returns = returns.dropna()
    
    # Step 5: Flag outliers (but don't remove — just report)
    mean = returns.mean()
    std  = returns.std()
    outlier_count = (returns.abs() > 3 * std).sum()
    if outlier_count > 0:
        print(f"INFO: {ticker} has {outlier_count} outlier days (>3σ)")
    
    # Step 6: Winsorize instead of removing
    returns = returns.clip(lower=mean - 3*std, upper=mean + 3*std)
    
    return returns


# Use it on multiple tickers with a list comprehension!
tickers = ["AAPL", "MSFT", "NVDA", "TLT", "GLD", "XOM"]

# Dictionary comprehension: {ticker: cleaned_returns}
# 'if r is not None' filters out any tickers that failed to download
cleaned = {}
for ticker in tickers:
    result = clean_pipeline(ticker, "2020-01-01", "2025-01-01")
    if result is not None:
        cleaned[ticker] = result

print(f"\nSuccessfully cleaned {len(cleaned)} out of {len(tickers)} tickers")

# Combine into a single DataFrame
# pd.DataFrame(cleaned) takes a dictionary of {column_name: Series}
# and turns it into a DataFrame with those columns
all_returns = pd.DataFrame(cleaned)
print(f"Shape: {all_returns.shape}")
print(all_returns.describe().round(4))
