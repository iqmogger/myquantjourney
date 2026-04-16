def get_sharpe(returns, risk_free_annual=0.04):
    daily_rf = risk_free_annual / 252
    mean_ret = returns.mean()
    vol = returns.std()
    sharpe = (mean_ret - daily_rf) / vol
    return sharpe

# "get_sharpe" gives back sharpe

# example:

import yfinance as yf

ticker = yf.download("AAPL", start='2023-01-01', end='2024-01-01')

returns = ticker['Close'].pct_change()

risk_free_annual = 0.04

mean_ret = returns.mean()

daily_rf = risk_free_annual / 252 

vol = returns.std()

sharpe = (mean_ret - daily_rf) / vol

print(sharpe) # Prints the same things as

get_sharpe(returns) # <--------- this
