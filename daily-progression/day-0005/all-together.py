import yfinance as yf
import numpy as np

def download_returns(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    returns = data['Close'].pct_change().dropna().squeeze()    # SQUEEZE IS VERY IMPORTANT
    return returns

def get_sharpe(returns, risk_free_annual=0.04):
    daily_rf = risk_free_annual / 252
    sharpe = (returns.mean() - daily_rf) / returns.std()
    return sharpe

def get_volatility(returns, annualize=True):
    vol = returns.std()
    if annualize:       # Basically if you put false then it's not gonna give you the annyalized result
        vol = vol * (252 ** 0.5)
    return vol


spy = download_returns('SPY', '2023-01-01', '2025-01-01')
aapl = download_returns('AAPL', '2023-01-01', '2025-01-01')

print(f"SPY  Sharpe: {get_sharpe(spy):.2f}  Vol: {get_volatility(spy):.4f}")
print(f"AAPL Sharpe: {get_sharpe(aapl):.2f}  Vol: {get_volatility(aapl):.4f}")
