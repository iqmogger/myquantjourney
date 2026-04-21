#Your strategy made money. But was it skill or noise? The t-stat tells you.
#Formula: t = mean / (std / sqrt(N))
#In words: how big is the signal divided by how wiggly the data is.
#Rule of thumb:

#|t| < 2 → noise
#|t| ≥ 3 → probably real
#|t| > 5 → suspicious (check for bugs/overfitting)


import numpy as np
import yfinance as yf

spy = yf.download("SPY", start="2020-01-01", end="2025-01-01",
                  auto_adjust=True, progress=False)
returns = spy["Close"].pct_change().dropna().squeeze()

t = returns.mean() / (returns.std() / np.sqrt(len(returns)))
print(f"T-stat: {t:.2f}")


