import yfinance as yf
import matplotlib.pyplot as plt

# Download AAPL
df = yf.download("AAPL", start="2023-01-01", end="2025-01-01")

# THE PROPER WAY — fig and ax
# fig = the whole image (the canvas)
# ax  = one chart area inside that image
# Think of fig as the piece of paper, ax as one graph drawn on it

fig, ax = plt.subplots()
# plt.subplots() returns TWO things at once — we learned this pattern
# with enumerate() on Day 8. Python lets you "unpack" into two variables.

# Now instead of plt.plot(), we use ax.plot()
ax.plot(df.index, df["Close"], color="steelblue", linewidth=0.8)

# ax has its own methods for labels and title
ax.set_title("AAPL Close Price", fontsize=14)
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")

# Add a grid — makes it easier to read values
# alpha controls transparency: 0 = invisible, 1 = fully solid
ax.grid(True, alpha=0.3)

plt.tight_layout()   # Prevents labels from getting cut off
plt.savefig("aapl_basic.png", dpi=150)
plt.show()
