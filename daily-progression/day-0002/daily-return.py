import yfinance as yf
import pandas as pd

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31") # Wrote this part myself ayy

# Daily Return is how much a stock gained or lost in a single day, expressed as a percentage
# Formula: (t − y) / y
# Where t = today's price   and   y = yesterday's price

df["Return"] = df["Close"].pct_change()   # pct change is very imporant. I'm guessing that it calculates the difference between each one.
print(df["Return"].describe())   # .describe is new, it looks at every number in that column and spits out a summary (below)

#count — how many rows have a value
#mean — the average return
#std — standard deviation (how much it bounces around)
#min — the worst single day
#25%, 50%, 75% — quartiles (the middle of the data split into chunks)
#max — the best single day
