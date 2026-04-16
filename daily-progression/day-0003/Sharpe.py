import pandas as pd
import yfinance as yf

# Download Apple stock for the last year
apple = yf.download('AAPL', start='2025-01-01', end='2026-01-01')

# Sharpe ratio = (avg return - risk-free rate) / volatility
# Risk-free rate ≈ 4% annual = 0.04/252 per day
# It answers: "How much return do I get per unit of risk?"
apple['Daily Return'] = apple['Close'].pct_change()

mean_return = apple['Daily_Return'].mean()
risk_free_rate = 0.04 / 252
sharpe = (mean_return - risk_free_rate) / volatility

print(f"Sharpe ratio: {sharpe:.2f}")
