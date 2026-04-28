import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

df = yf.download("SPY", start="2020-01-01", end="2025-01-01")
returns = df["Close"].pct_change().dropna()

# Find the worst day
worst_day = returns.idxmin()       # returns the DATE of the minimum value
worst_return = returns.min()       # the actual return value
worst_price = df.loc[worst_day, "Close"]  # price on that day

# Find the best day
best_day = returns.idxmax()
best_return = returns.max()
best_price = df.loc[best_day, "Close"]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df["Close"], color="steelblue", linewidth=0.7)

# NEW — annotate() places text with an arrow pointing to a data point
ax.annotate(
    f"Worst: {worst_return:.1%}",    # Text to display (.1% formats as percentage)
    xy=(worst_day, worst_price),      # Where the arrow POINTS TO (the data point)
    xytext=(worst_day, worst_price + 80),  # Where the TEXT sits
    fontsize=9,
    color="firebrick",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="firebrick", lw=1.2)
    # arrowprops is a dictionary (Day 8!) controlling the arrow appearance
    # arrowstyle="->" draws a simple arrow
    # lw = linewidth of the arrow
)

ax.annotate(
    f"Best: {best_return:.1%}",
    xy=(best_day, best_price),
    xytext=(best_day, best_price + 80),
    fontsize=9,
    color="forestgreen",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="forestgreen", lw=1.2)
)

# NEW — ax.text() places text at a specific position
# transform=ax.transAxes means coordinates are 0-1 fractions of the chart
# (0, 0) = bottom-left, (1, 1) = top-right
ax.text(0.02, 0.95, f"Total Return: {(df['Close'].iloc[-1]/df['Close'].iloc[0] - 1):.1%}",
        transform=ax.transAxes, fontsize=11, fontweight="bold",
        verticalalignment="top")

ax.set_title("SPY 2020–2025 with Key Events", fontsize=14, fontweight="bold")
ax.set_ylabel("Price ($)")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("spy_annotated.png", dpi=150)
plt.show()
