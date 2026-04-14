# Day 0003 — Time Series Analysis & Financial Metrics

## What I Learned

### Terms / Concepts:
- **Index** — Row labels in a DataFrame (like dates in stock data). Lets you slice data by time easily without complicated filtering.
- **Rolling Window** — A sliding window that moves through data one row at a time, calculating something (like average) at each step. Used to smooth out noise.
- **Moving Average (MA)** — The average of the last N closing prices. Filters out daily noise to show the real trend. If price > 20-day MA, stock is trending up.
- **`.rolling(window=N)`** — Pandas function to create a rolling window of size N and calculate statistics on it.
- **`.mean()`** — Calculates the average. **Must include ()** to actually call the function (not just reference it).
- **Daily Volatility** — Standard deviation of daily returns. Measures how much a stock bounces around each day (e.g., ±0.81% per day).
- **Annualized Volatility** — Daily volatility scaled to a full year by multiplying by √252. Shows expected yearly swings (e.g., ±12.82% per year).
- **√252** — The magic conversion factor. 252 = trading days per year. Converts any daily metric to annual metric.
- **Risk-Free Rate** — Return from a "safe" investment like US Treasury bonds. Assumed ~4% annually or 0.04/252 per day.
- **Sharpe Ratio** — Risk-adjusted return metric. Formula: (avg return − risk-free rate) / volatility. Shows how much return you get per unit of risk. Higher is better (>1.0 is good, >2.0 is exceptional).
- **Formatting Code (`.4f`, `.2f`)** — Controls decimal places when printing. The `:` separates the variable from the format instruction (e.g., `{volatility:.4f}` shows 4 decimal places).

### Coding:
- How to use `.rolling(window=N).mean()` to calculate moving averages
- How to annualize daily metrics (multiply by √252)
- How to calculate Sharpe ratio from scratch
- Proper f-string formatting with colons (not parentheses)
- Column naming consistency (spaces vs underscores matter!)

## The Code
There's 3 files and 1 "assignment"

## Questions I Answered

**Q1: What is the difference between a moving average and daily returns?**
- Moving average is the average of the last N closing prices — it smooths out noise and shows the trend.
- Daily returns are the percent change from day to day — they're the raw signal that strategies are built on.
- Both are useful: MA shows direction, returns show volatility.

**Q2: Why do we annualize volatility?**
- Daily volatility (0.0081) seems tiny and doesn't give you perspective.
- Annualized volatility (0.1282) shows how much risk compounds over a full year.
- It's easier to understand "expect ±12.82% swings per year" than "±0.81% per day."

**Q3: What does a Sharpe ratio of 0.10 tell you about SPY's performance?**
- It's on the low side. A Sharpe of 0.10 means you only get 0.10% return per 1% of risk.
- Good strategies have Sharpe > 1.0. SPY didn't have great returns relative to its risk over 2023-2025.
- I wouldn't invest based on this alone — but broad market indexes are steady and safe, even if Sharpe is low.

**Q4: If you calculated the same metrics for a different stock (like AAPL or TSLA), what would be different?**
- AAPL and TSLA would have higher daily volatility than SPY (they're more volatile than the broad market).
- Their annualized volatility would be higher (maybe 25-35% instead of 12.82%).
- Their Sharpe ratios could be higher OR lower depending on how much they actually gained vs how much they bounced around.

**Q5: What bug did you encounter in your code, and how did you fix it?**
- I created a column called `'Daily Return'` (with a space) but tried to access it as `'Daily_Return'` (with an underscore).
- Python treated these as different column names and threw a KeyError.
- Fix: Keep the column name consistent — use the exact same name everywhere, either with space or underscore.

## Key Takeaway
Moving averages smooth trends, volatility measures risk, and Sharpe ratio combines both into one number that tells you if a strategy is worth the risk.
