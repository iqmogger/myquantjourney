import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tickers = ["XLK", "XLF", "XLE", "XLV", "XLY"]

data = yf.download(tickers, start="2019-01-01", end="2025-01-01")

prices = data["Close"]

def sma_backtest(prices, fast=20, slow=50):
  sma_fast = prices.rolling(fast).mean()
  sma_slow = prices.rolling(slow).mean()
  signal = pd.Series(np.where(sma_fast > sma_slow, 1, 0), index=prices.index)
  position = signal.shift(1)
  daily = prices.pct_change()
  strategy_return = daily * position
  return strategy_return, daily

def calc_metrics(returns):
  std = returns.std()
  mean = returns.mean()
  equity = (1 + returns).cumprod()
  years = len(equity) / 252
  N = len(returns)
  #=================
  sharpe = (mean / std) * np.sqrt(252)
  cagr = equity.iloc[-1] ** (1/years) - 1
  max_dd = (equity / (equity.cummax()) - 1).min()
  calmar = cagr / np.abs(max_dd)
  tstat = mean / (std / np.sqrt(N))
  return {
  "Sharpe": sharpe,
  "CAGR": cagr,
  "Max Drawdown": max_dd,
  "Calmar": calmar,
  "T-Stat": tstat
  }

results = {}
for ticker in tickers:
  try:
    ticker_prices = prices[ticker]
    strat_returns, daily_returns = sma_backtest(ticker_prices)
    metrics = calc_metrics(strat_returns)
    results[ticker] = metrics
  except:
    print(f"{ticker} failed")
    
table = pd.DataFrame.from_dict(results, orient="index")
table = table.sort_values("Sharpe", ascending=False)
print("\n-- SMA Crossover Results --\n")
print(table.round(4))

plt.figure(figsize=(10, 6))

plt.bar(table.index, table["Sharpe"])
plt.title("Sharpe Graph: XL_")
plt.ylabel("Sharpe")
plt.savefig("sector_showdown.png")
plt.show()
