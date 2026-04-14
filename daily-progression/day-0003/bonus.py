import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(spy['Close'], label='SPY Close', alpha=0.7)
plt.plot(spy['SMA_50'], label='50-Day SMA', color='red')
plt.legend()
plt.title('SPY Price vs Moving Average')
plt.show()


# Plot. That's it.
