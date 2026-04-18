import pandas as pd

s = pd.Series([100, 120, 110, 150, 130, 160])
print(s.cummax())
# 0    100
# 1    120
# 2    120   <- didn't go above 120
# 3    150   <- new peak
# 4    150   <- still below 150
# 5    160   <- new peak

#drawdown = (equity_curve - equity_curve.cummax()) / equity_curve.cummax()
