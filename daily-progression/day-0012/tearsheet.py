import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

df = yf.download("SPY", start="2020-01-01", end="2025-01-01")
returns = df["Close"].pct_change().dropna()

# ── Calculate metrics (all from previous days!) ──
# Cumulative return (Day 6)
cumulative = (1 + returns).cumprod()

# Drawdown (Day 7)
peak = cumulative.cummax()
drawdown = (cumulative - peak) / peak

# Rolling 21-day volatility, annualized (Day 3)
rolling_vol = returns.rolling(21).std() * np.sqrt(252)

# ── Build the figure: 3 rows, 1 column ──
# sharex=True makes all panels share the same x-axis (dates)
# This means zooming one panel zooms them all — dates stay aligned
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# NEW — height_ratios: make the top panel taller than the others
# gridspec_kw is a dictionary (Day 8!) of grid settings
# height_ratios=[3, 1, 1] means: top panel gets 3 parts of height,
# middle and bottom each get 1 part. So top is 3x taller.
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True,
                          gridspec_kw={"height_ratios": [3, 1, 1]})

# ── Panel 1: Cumulative Return ──
axes[0].plot(cumulative.index, cumulative, color="steelblue", linewidth=0.9)
axes[0].set_title("SPY Tearsheet (2020–2025)", fontsize=14, fontweight="bold")
axes[0].set_ylabel("Growth of $1")
axes[0].grid(True, alpha=0.3)
# NEW — axhline draws a HORIZONTAL line across the whole panel
# Here we draw a dashed line at y=1.0 (the starting value)
axes[0].axhline(y=1.0, color="gray", linestyle="--", linewidth=0.7)

# ── Panel 2: Drawdown ──
# fill_between shades the area between two y-values
# Here we shade from the drawdown line down to 0 (so the red area shows losses)
axes[1].fill_between(drawdown.index, drawdown, 0, color="firebrick", alpha=0.4)
axes[1].set_ylabel("Drawdown")
axes[1].grid(True, alpha=0.3)

# ── Panel 3: Rolling Volatility ──
axes[2].plot(rolling_vol.index, rolling_vol, color="darkorange", linewidth=0.8)
axes[2].set_ylabel("21d Ann. Vol")
axes[2].set_xlabel("Date")
axes[2].grid(True, alpha=0.3)
# NEW — axhline at the median volatility for reference
axes[2].axhline(y=rolling_vol.median(), color="gray", linestyle="--", linewidth=0.7)

plt.tight_layout()
plt.savefig("spy_tearsheet.png", dpi=150)
plt.show()
