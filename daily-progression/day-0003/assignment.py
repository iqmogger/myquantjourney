import yfinance as yf
import pandas as pd

sp = yf.download("SPY", start="2023-01-01", end="2025-01-01")

sp['50 Day MA'] =  sp['Close'].rolling(window=50).mean()


sp['Daily_Return'] = sp['Close'].pct_change()

volatility = sp['Daily_Return'].std()
print(f"Daily Volatility: {volatility:.4f}")

ann_vol = volatility * (252 ** 0.5)
print(f"Annual volatility: {ann_vol:.4f}")


mean_return = sp['Daily_Return'].mean()
risk_free_rate = 0.04 / 252
sharpe = (mean_return - risk_free_rate) / volatility

print(f"Sharpe ratio: {sharpe:.2f}")
