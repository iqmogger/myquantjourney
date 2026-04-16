#functions with multiple outputs also exist!
import yfinance as yf

ticker = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

returns = ticker['Close'].pct_change().squeeze()    # Squeeze turns a datafram into a series. Makes it so .4f actually works


def analyze_stock(returns):
    vol = returns.std() * (252 ** 0.5)
    sharpe = (returns.mean() - 0.04/252) / returns.std()
    max_return = returns.max()
    min_return = returns.min()
    return vol, sharpe, max_return, min_return

v, s, best, worst = analyze_stock(returns)
print(f"Volatility: {v:.4f}")
print(f"Sharpe: {s:.2f}")
print(f"Best day: {best:.4f}")
print(f"Worst day: {worst:.4f}")
