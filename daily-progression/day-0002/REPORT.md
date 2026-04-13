# day 0002 — Pandas

## what i learned
Terms / concepts:
- Daily Return — how much a stock gained or lost in a single day, expressed as a percentage. Formula: (today's price − yesterday's price) / yesterday's price. This is the raw signal almost every strategy is built on.

- Volatility — how much a stock's returns bounce around. Measured by the standard deviation of daily returns. High vol = big swings = higher risk and higher potential reward. NVDA is much more volatile than, say, a bank stock.

- Descriptive Statistics — the summary numbers from .describe(): mean, std, min, max, quartiles. Before building any strategy, you always describe your data first.

Coding:
- How to find the daily return
- How to use pandas (sorta, need practice though):
    - .head
    - .tail
    - .shape
    - .columns
    - .dtypes
    - etc.
- Basic filtering. 




## the code
three files: `daily-return.py`, `pandas.py`, `filtering.py`

## questions i answered
- What does df.shape return for AAPL 2024? What do the two numbers mean?
  - Returns (row, column). Gives the general shape: how many columns and rows are there? 
    
- What is the mean daily return from .describe()? Is it positive or negative?
  - 0.001345 or 0.1%. Positive.
    
- What is the std (standard deviation) of daily returns? What does that tell you about risk?
  - 0.014 or 1.4%. Normal volatility. 
    
- How many days did AAPL go up more than 2%? How many did it drop more than 2%? Is it symmetric?
  - Went down 17 days. Not symmertric, there were only 14 days going up more than 2%.
    
- Change the ticker to "NVDA" in returns.py. Is NVDA's standard deviation higher or lower than AAPL's? What does that mean?
  - Higher. 3.3%. Volatile. More risky.
