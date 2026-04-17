THIS IS VERY VERY VERY IMPORTANT
This is how every single strategy backtest works, they all follow this pipeline. Memorize this.


1. Download price data
2. Calculate features (moving averages, volatility, etc.)
3. Generate signal (True/False condition)
4. Convert signal to position (1/0/-1)
5. Shift position by 1 day (avoid lookahead)
6. Multiply shifted position by next-day return = strategy return
7. Cumulative strategy return = performance
