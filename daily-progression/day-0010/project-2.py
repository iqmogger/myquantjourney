import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tickers = ["BA", "AAPL", "NVDA", "NKE", "HD"]
data = yf.download(tickers, start="2020-01-01", end="2025-01-01")
prices = data["Close"]
daily = prices.pct_change().dropna()

def portfolio_sharpe(weights, daily_returns):
  port_ret = (daily_returns * weights).sum(axis=1)
  std = port_ret.std()
  mean = port_ret.mean()
  #===========
  sharpe = (mean / std) * np.sqrt(252)
  return sharpe
  
best_sharpe = -1
best_weights = None

for i in range(100000):
  w = np.random.random(5)
  w = w / w.sum()
  sharpe = portfolio_sharpe(w, daily)
  if sharpe > best_sharpe:
    best_sharpe = sharpe
    best_weights = w

print(f"\nBest Sharpe: {best_sharpe:.4f}\n")
for ticker, weight in zip(tickers, best_weights):
    print(f"{ticker}: {weight:.2%}")

plt.figure(figsize=(8, 8))
plt.pie(best_weights, labels=tickers, autopct="%.1f%%")
plt.title("Optimal Portfolio Weights")
plt.savefig("portfolio_builder.png")
plt.show()
