# Day 0011 — List Comprehensions & Data Cleaning

## What I Learned
- List slicing: `list[start:stop]`, negative indices like `list[-2:]`
- `len()` for list length, `in` for membership check
- `.append()` to add, `.remove()` to delete items from a list
- List comprehensions: `[expr for item in list]` — one-line list building
- Filtered comprehensions: `[expr for item in list if condition]`
- Dictionary comprehensions: `{key: val for item in list}`
- `%` modulo operator — gives remainder of division
- NaN: pandas placeholder for missing data
- `.isna().sum()` to count missing values
- `.dropna()` removes NaN rows, `.fillna(0)` replaces them with a value
- `.fillna(method="ffill")` forward fills with last known value
- `.abs()` for absolute value
- `.clip(lower, upper)` to cap extreme values (winsorizing)
- Docstrings: `"""description"""` inside functions for documentation
- `None` — Python's "nothing" value, used when a function has no result to give
- `as e` in `except Exception as e` saves the error message into a variable

## The Code
- `lists_deep.py` — slicing, len, in, append, remove
- `list_comp.py` — list comprehensions and dictionary comprehensions
- `cleaning.py` — NaN detection, dropna, fillna, ffill
- `outliers.py` — finding outlier days beyond 3σ, removing vs winsorizing
- `pipeline.py` — full clean_pipeline() function across 6 tickers

## Questions

**Q1: What's the difference between dropna() and fillna(0) for returns data? When would you use each?**
dropna() deletes the row entirely — the day disappears from your dataset. fillna(0) keeps the row but says "no change happened." For returns, fillna(0) is usually better because dropping rows messes up your date alignment if you're comparing multiple stocks. But for the first NaN from pct_change(), either works since there's genuinely no prior day to compare to.

**Q2: Why is winsorizing usually better than deleting outliers in financial data?**
Deleting an outlier removes a real trading day from your backtest. If March 2020 had a -10% crash and you delete it, your backtest pretends that day didn't exist — your strategy would have had to survive it in real life. Winsorizing caps it (say at -6%) so the day still counts, the pain is still there, but one extreme point doesn't dominate your statistics.

**Q3: You see a stock with a -40% daily return. Real crash or data error?**
Check the date — was there news (earnings disaster, fraud, delisting)? Check other stocks on the same day — if SPY also dropped, it's probably real. Check the price the next day — if it snaps back to normal, the -40% was likely a bad data point. Check volume — real crashes have huge volume. If it's just one stock, no news, price recovers next day, low volume — it's a data error.

**Q4: Write the list comprehension for [1, -2, 3, -4, 5] returning only positives. Then write it as a for loop.**
Comprehension: `[n for n in [1, -2, 3, -4, 5] if n > 0]`
Loop version: start with `result = []`, then `for n in [1, -2, 3, -4, 5]:` then `if n > 0:` then `result.append(n)`. The comprehension is easier to read once you're used to the pattern — it keeps the logic on one line instead of four.

**Q5: Your pipeline downloads 20 tickers but 3 fail. Why return None instead of crashing?**
If the function crashes on ticker #4, you lose tickers 5 through 20 — all that data gone because of one bad download. Returning None lets the loop skip the failure and keep going. At the end you have 17 clean tickers instead of 0. This is the same try/except + continue pattern from Day 9 but wrapped inside a function.

## Reflection
Data cleaning isn't glamorous but it's where real quant work lives. A backtest on dirty data is worse than no backtest — it gives you false confidence. List comprehensions make the cleaning code compact enough that you can actually read a whole pipeline without scrolling for five minutes.
