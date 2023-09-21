import pandas as pd
import pyupbit

def get_rsi(ticker, interval="minute3"):
    df = pyupbit.get_ohlcv(ticker, interval=interval)
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)

    avg_gain = gain.rolling(window=14, min_periods=1).mean()
    avg_loss = loss.rolling(window=14, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi

rsi_values = get_rsi(ticker)
print(rsi_values)