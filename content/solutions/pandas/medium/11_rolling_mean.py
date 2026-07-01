def rolling_mean(s, window: int):
    return s.rolling(window, min_periods=1).mean()
