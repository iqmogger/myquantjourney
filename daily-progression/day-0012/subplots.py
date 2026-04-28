import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2023-01-01", end="2025-01-01")
returns = df["Close"].pct_change()

# Create a figure with 2 rows, 1 column of charts
# fig = the whole image
# axes = a LIST of ax objects — one per panel
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
# 2 = rows, 1 = column
# figsize=(12, 8) = width 12 inches, height 8 inches

# axes[0] is the TOP panel
# axes[1] is the BOTTOM panel
# This is list indexing from Day 11!

# ── Top panel: Price ──
axes[0].plot(df.index, df["Close"], color="steelblue", linewidth=0.8)
axes[0].set_title("AAPL Close Price", fontsize=13)
axes[0].set_ylabel("Price ($)")
axes[0].grid(True, alpha=0.3)

# ── Bottom panel: Daily Returns ──
# .bar() makes a bar chart instead of a line chart
# Great for returns because you can see positive (green) vs negative (red)
colors = ["forestgreen" if r >= 0 else "firebrick" for r in returns.dropna()]
# ^ That's a LIST COMPREHENSION from Day 11!
# For each return: if it's >= 0, use green; otherwise, use red

axes[1].bar(returns.dropna().index, returns.dropna(), color=colors, width=1.0)
axes[1].set_title("Daily Returns", fontsize=13)
axes[1].set_ylabel("Return")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("aapl_two_panel.png", dpi=150)
plt.show()
