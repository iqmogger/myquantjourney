"""
Day 0007 — Concept 1: What Is a Drawdown?
A walkthrough of the drawdown concept using a tiny fake portfolio.
"""

import pandas as pd

# A drawdown is the PERCENTAGE DECLINE from the most recent peak
# in your equity curve.

# Imagine your portfolio goes $100 → $150 → $120 → $180.
portfolio = pd.Series([100, 150, 120, 180])
print("Portfolio values:")
print(portfolio)
print()

# At the $120 point, you're in a drawdown — you're 20% below
# your $150 peak. Once you hit $180, the drawdown ends and a
# new peak is set.

# Key insight: drawdown is measured from the RUNNING MAXIMUM,
# not from the start. Every new high resets the reference point.
running_max = portfolio.cummax()
print("Running max (the 'peak so far' at each point):")
print(running_max)
# 0    100   (only seen 100)
# 1    150   (new peak)
# 2    150   (120 didn't beat 150)
# 3    180   (new peak)
print()

# Drawdown at each point = (current - peak) / peak
drawdown = (portfolio - running_max) / running_max
print("Drawdown at each point:")
print(drawdown)
# 0     0.00   (at the peak)
# 1     0.00   (new peak, so at the peak again)
# 2    -0.20   (20% below 150)
# 3     0.00   (new peak, drawdown reset)
print()

# Three numbers matter in real analysis:
# 1. MAX DRAWDOWN — the worst peak-to-trough loss ever suffered
max_dd = drawdown.min()
print(f"Max drawdown: {max_dd:.2%}")

# 2. DRAWDOWN DURATION — how many periods spent below the peak
#    (we'll dig into this as the bonus challenge later)

# 3. CURRENT DRAWDOWN — how far below the all-time high right now
current_dd = drawdown.iloc[-1]
print(f"Current drawdown: {current_dd:.2%}")
print()

# A strategy with 20% annual return and 10% max drawdown is
# VASTLY better than one with 20% annual return and 50% max
# drawdown. Same return, wildly different experience of holding it.
