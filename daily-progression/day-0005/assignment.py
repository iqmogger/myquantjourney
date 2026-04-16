import numpy as np
import yfinance as yf
import pandas as pd

def download_data(ticker, start, end):
  data = yf.download(ticker, start=start, end=end)
  returns = data['Close'].pct_change().dropna().squeeze()
  return returns

def get_sharpe(returns, risk_free_annual=0.04):
  daily_rf = risk_free_annual / 252
  avg_r = returns.mean()
  sharpe = (avg_r - daily_rf) / returns.std()
  return sharpe

def get_vol(returns, annualize = True):
  vol = returns.std()
  if annualize:     
        vol = vol * (252 ** 0.5)
  return vol

def compare_stocks(tickers, start, end):
  for ticker in tickers:
    returns = download_data(ticker, start, end)
    sharpe = get_sharpe(returns, risk_free_annual=0.04)
    vol = get_vol(returns, annualize = True)
    print(sharpe, vol)

tickers = ['AAPL', 'SPY']
compare_stocks(tickers, '2023-01-01', '2025-01-01')
