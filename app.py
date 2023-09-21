import pyupbit
import asyncio
from websocket_handler import main
from calculate_rsi import get_rsi

from dotenv import load_dotenv
load_dotenv()
import pandas as pd
# 이제 환경변수에 접근할 수 있습니다.
import os
access_key = os.getenv("UPBIT_OPEN_API_ACCESS_KEY")
secret_key = os.getenv("UPBIT_OPEN_API_SECRET_KEY")

#로그인  upbit 객체를 사용해 주문, 잔고 조회등 할 수 있음.
upbit = pyupbit.Upbit(access_key, secret_key)

ticker= "KRW-BTC"

def handler(ticker):
    print(ticker)

asyncio.get_event_loop().run_until_complete(main())

# 원하는 코인의 실시간 가격 정보를 받음
pyupbit.UpbitWebsocket().run(["ticker:KRW-BTC"], handler)

rsi = get_rsi(ticker)
