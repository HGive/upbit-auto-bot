import pyupbit
import time
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

# 이제 환경변수에 접근할 수 있습니다.

access_key = os.getenv("UPBIT_OPEN_API_ACCESS_KEY")
secret_key = os.getenv("UPBIT_OPEN_API_SECRET_KEY")

#로그인  upbit 객체를 사용해 주문, 잔고 조회등 할 수 있음.
upbit = pyupbit.Upbit(access_key, secret_key)

# 타겟 종목 , 인터발
ticker = "KRW-AXS"
interval = "minute3"
target_rsi = 77
buy_count = 0

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


while True:
    #잔고
    balance = upbit.get_balance("KRW")
    print(balance)
    #RSI 구하기
    rsi = get_rsi(ticker, interval)
    print(rsi)

    #지정가 매수 주문
    if rsi < target_rsi and buy_count < 2 :
        target_price = pyupbit.get_current_price(ticker)*0.9
        # upbit.buy_limit_order(ticker,target_price,)
        print("매수")
        buy_count +=1

    print("----------")
    #지정가 매도 주문
    # upbit.sell_limit_order()
    time.sleep(1)