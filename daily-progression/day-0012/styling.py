import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# ── STYLE SETTINGS ──
# You can set defaults that apply to ALL your charts
# plt.rcParams is a dictionary (Day 8!) of matplotlib settings
plt.rcParams["figure.facecolor"] = "white"       # background color
plt.rcParams["axes.facecolor"]   = "#FAFAFA"      # chart area background (very light gray)
plt.rcParams["axes.edgecolor"]   = "#CCCCCC"      # border around chart
plt.rcParams["axes.labelsize"]   = 11             # axis label font size
plt.rcParams["xtick.labelsize"]  = 9              # x-axis tick font size
plt.rcParams["ytick.labelsize"]  = 9              # y-axis tick font size
plt.rcParams["grid.alpha"]       = 0.3            # grid transparency
plt.rcParams["font.family"]      = "sans-serif"   # clean font

df = yf.download("NVDA", start="2023-01-01", end="2025-01-01")
returns = df["Close"].pct_change().dropna()

fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True,
                          gridspec_kw={"height_ratios": [2, 1]})

# ── Price with Moving Averages ──
axes[0].plot(df.index, df["Close"], color="#1976D2", linewidth=0.8, label="Close")
# NEW — label="..." names this line for the legend

sma_50 = df["Close"].rolling(50).mean()
sma_200 = df["Close"].rolling(200).mean()

axes[0].plot(df.index, sma_50, color="#FF9800", linewidth=1.0,
             linestyle="--", label="50-day SMA")
axes[0].plot(df.index, sma_200, color="#E91E63", linewidth=1.0,
             linestyle="--", label="200-day SMA")

# NEW — legend() shows a box explaining which color is which line
# loc="upper left" places it in the top-left corner
# framealpha controls the legend box transparency
axes[0].legend(loc="upper left", fontsize=9, framealpha=0.8)
axes[0].set_title("NVDA — Price & Moving Averages", fontsize=14, fontweight="bold")
axes[0].set_ylabel("Price ($)")
axes[0].grid(True)

# ── Return Distribution (Histogram) ──
# NEW — hist() draws a histogram: it groups values into "bins" (buckets)
# and shows how many values fall into each bucket
axes[1].hist(returns, bins=80, color="#1976D2", alpha=0.7, edgecolor="white",
             linewidth=0.3)
# bins=80 means divide the range of returns into 80 buckets
# edgecolor="white" puts a thin white border around each bar so they don't blur together

axes[1].set_title("Return Distribution", fontsize=13)
axes[1].set_xlabel("Daily Return")
axes[1].set_ylabel("Frequency")
# NEW — axvline draws a VERTICAL line (compare with axhline = horizontal)
axes[1].axvline(x=0, color="gray", linestyle="--", linewidth=0.7)
axes[1].axvline(x=returns.mean(), color="firebrick", linestyle="-", linewidth=1.0,
                label=f"Mean: {returns.mean():.4f}")
axes[1].legend(fontsize=9)
axes[1].grid(True)

plt.tight_layout()
plt.savefig("nvda_styled.png", dpi=150)
plt.show()
