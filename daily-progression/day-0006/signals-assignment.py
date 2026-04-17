import yfinance as yf
import pandas as pd
import numpy as np

data = yf.download('SPY', start='2020-01-01', end='2026-01-01', auto_adjust=True)
data.columns = data.columns.droplevel(1)   # droplevel removes the second column

# Calculate two moving averages
data['SMA_fast'] = data['Close'].rolling(window=20).mean()    # SMA_20 basically. SMA = Simple Moving Average
data['SMA_slow'] = data['Close'].rolling(window=50).mean()     # SMA_50

# Signal: be long when fast SMA > slow SMA (classic "golden cross" logic)
data['signal'] = np.where(data['SMA_fast'] > data['SMA_slow'], 1, 0)

# Shift to avoid lookahead bias
data['position'] = data['signal'].shift(1)    # Just a shift 

# Daily returns
data['daily_return'] = data['Close'].pct_change()   

data['strategy_return'] = data['position'] * data['daily_return']


# Cumulative returns
data['cum_strategy'] = (1 + data['strategy_return']).cumprod()
data['cum_buyhold'] = (1 + data['daily_return']).cumprod()

# Total returns
total_strategy = data['cum_strategy'].iloc[-1] - 1
total_buyhold = data['cum_buyhold'].iloc[-1] - 1         # .iloc stands for integer location. It's how you grab rows or values by their numerical position.

def get_sharpe(returns, risk_free_annual=0.04):
    daily_rf = risk_free_annual / 252
    mean_ret = returns.mean()
    vol = returns.std()
    return (mean_ret - daily_rf) / vol * (252 ** 0.5)

strategy_sharpe = get_sharpe(data['strategy_return'].dropna())
buyhold_sharpe = get_sharpe(data['daily_return'].dropna())


print("=" * 50)      # basically makes it cleaner. its a string of 50 =. Looks like this: ===============     acts as a separator
print("SMA CROSSOVER STRATEGY: 20 over 50")       # Strategy name, still just formatting
print("=" * 50)  # again
print(f"Strategy total return: {total_strategy:.2%}")    
print(f"Buy & hold return:     {total_buyhold:.2%}")
print(f"Strategy Sharpe:       {strategy_sharpe:.2f}")
print(f"Buy & hold Sharpe:     {buyhold_sharpe:.2f}")     # the rest is just data.


#------------- NOTES --------------


#The trading logic: When the 20-day average is above the 50-day average, it means prices over the last 20 days have been higher than over the last 50 days — i.e., the stock is in an uptrend. So the rule says "be long during uptrends, be flat during downtrends."


#----------------------------------

# Here's how to remove the ... in the output:

# pd.set_option('display.max_rows', None)
# This is if you want it for all

# with pd.option_context('display.max_rows', None):
#    print(data)
# if you want it only for 1 thing

# But most of the time you'd look at charts


#----------------------------------



#Result:

#==================================================
#SMA CROSSOVER STRATEGY: 20 over 50
#==================================================
#Strategy total return: 65.80%
#Buy & hold return:     129.06%
#Strategy Sharpe:       0.43
#Buy & hold Sharpe:     0.58
