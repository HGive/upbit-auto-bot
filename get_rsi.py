import pyupbit
import pandas as pd
import numpy as np

# pd.set_option('display.float_format', lambda x: '%.2f' % x)

def get_rsi(ticker, interval):
    df = pyupbit.get_ohlcv(ticker, interval= interval)

    df['변화량'] = df['close'] - df['close'].shift(1)
    df['상승폭'] = np.where(df['변화량']>=0, df['변화량'], 0)
    df['하락폭'] = np.where(df['변화량'] <0, df['변화량'].abs(), 0)
    # welles moving average
    df['AU'] = df['상승폭'].ewm(alpha=1/14, min_periods=14).mean()
    df['AD'] = df['하락폭'].ewm(alpha=1/14, min_periods=14).mean()
    df['RSI'] = df['AU'] / (df['AU'] + df['AD']) * 100
    return df[['RSI']].iloc[-1].RSI


rsi = get_rsi("KRW-BTC","minute3")