import yfinance as yf
import pandas as pd

df = yf.download("AAPL", start="2024-01-01", end="2024-12-31")

df["Return"] = df["Close"].pct_change()   
print(df["Return"].describe())  

# Find all days where the stock went up more than 2%
big_up_days = df[df["Return"] > 0.02]     
# There are 2 df's because the one inside, df["return"], checks every row in the returns colums asking "is this greater than 0.2?" It gives back "True" or "False"
# The second one is the flter. It goes like "Only keep the ones that are true."
print(f"Days up more than 2%: {len(big_up_days)}")    # Length. Gives you the # of days.


# Find all days where it dropped more than 2%
big_down_days = df[df["Return"] < -0.02]
print(f"Days down more than 2%: {len(big_down_days)}")  
