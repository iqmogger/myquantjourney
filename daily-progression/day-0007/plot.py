import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Make some fake data — 100 days of a random-walk "price"
np.random.seed(42)  # makes the randomness reproducible.   Random number generators aren't actually random, they're based on a starting number called a "seed."
daily_changes = np.random.randn(100) * 0.01  # small random daily % moves
fake_price = 100 * (1 + pd.Series(daily_changes)).cumprod()

# ---- The 5-line matplotlib pattern ----

plt.figure(figsize=(12, 6))   # create a blank canvas, 12 wide × 6 tall
plt.plot(fake_price)          # draw a line using the Series values
plt.title("Fake Price Over 100 Days")    # title
plt.xlabel("Day")    # x axis is "Day"
plt.ylabel("Price ($)")   # y axis is "Price ($)"
plt.grid(True)                # adds gridlines — easier to read
plt.show()                    # actually display the chart
