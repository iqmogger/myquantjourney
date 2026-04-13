import yfinance as yf
import pandas as pd

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31") # Wrote this part myself ayy

# Data below
print(df.head()) # New! ".head" prints the first 5 rows by default. You can change the #
print(df.tail(3)) # prints the last 3 rows.
print(df.shape) # prints the rows and columns of the data (rows, columns)
print(df.columns) # gives you all the columns (whatever was downloaded in df)
print(df.dtypes) # good bc if there's text in a column of numbers then it will crash.  


# Series is like 1 column of a DataFrame, which is the full table
close = df["Close"]  # returns a Series, grabs the column
print(type(close))   # gives you the type like is it a series or a dataframe. For some reason it returned dataframe. 

# Access multiple columns
subset = df[["Close", "Volume"]]

# Access a specific ROW by date
print(df.loc[2024-06-05]) # Grabs a specific row. Since they're sorted by date, we need to put the date there to get it.

# Access a range of rows
print(df.loc["2024-06-01":"2024-06-30"]) # Same thing, just with a range.

