import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

spy = yf.download("SPY", start="2015-01-01", end="2025-01-01",
                  auto_adjust=True, progress=False)
returns = spy["Close"].pct_change().dropna().squeeze()

rolling_sharpe = (returns.rolling(252).mean() / returns.rolling(252).std()) * np.sqrt(252)

plt.figure(figsize=(12, 5))
plt.plot(rolling_sharpe)
plt.axhline(0, color="black", linewidth=0.5)
plt.title("SPY — 1-Year Rolling Sharpe")
plt.grid(alpha=0.3)
plt.show()
