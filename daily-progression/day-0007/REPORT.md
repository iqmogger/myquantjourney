# Day 0007 — Drawdowns & Honest Performance Metrics

## What I Learned
### Concepts:
- Drawdown = how far below the all-time peak you are at any point
- Max drawdown matters because it determines whether you'd actually stick with a strategy
- CAGR = the steady annual rate that compounds to your total return
- Calmar ratio = CAGR / |max drawdown| — return per unit of pain
- Equity curve = the line showing what $1 becomes over time

### Coding:
- .cummax() for tracking the running peak
- matplotlib: figure, plot, subplots, fill_between, savefig
- Writing a reusable summarize() function with f-string formatting
- .index to access DataFrame row labels (dates)

## Questions

Q1: What is a drawdown, and why is it measured from the running peak
instead of from the starting value?
Because you're calculating max losses from a peak

Q2: Your strategy returned 65.80% vs buy-and-hold's 129.06%. But their
Sharpe ratios were nearly identical (0.75 vs 0.77). How is that possible?
The ratios were right.

Q3: What does a Calmar ratio of 0.44 vs 0.31 tell you? Which strategy
does it favor and why?
Favors the 0.44 calmar startegy. Means it has a better risk to return ratio

Q4: If someone showed you a strategy with 50% annual return and -80%
max drawdown, would you trade it? Why or why not?
Definitely not. You lose 80% one time and that's enough for anyone to sell.

Q5: What does .cummax() do and why is it the key to calculating drawdown?
Formula:
data['buyhold_peak'] = data['buyhold_equity'].cummax()
data['buyhold_dd'] = (data['buyhold_equity'] - data['buyhold_peak']) / data['buyhold_peak']
you need cummax() to calculate the peak. You need the peak to calculate DD
