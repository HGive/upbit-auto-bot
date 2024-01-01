import multiprocessing as mp
import pyupbit
import time

buy_count = 0 

while True : 
    buy_count +=1
    if buy_count <=2:
        print(buy_count , " 매수")
    else :
        print("---")

    if buy_count >=6:
        buy_count = 0
    time.sleep(1)

# if __name__ == "__main__":
#     queue = mp.Queue()
#     proc = mp.Process(
#         target=pyupbit.WebSocketClient,
#         args=('ticker', ["KRW-BTC"], queue),
#         daemon=True
#     )
#     proc.start()

#     while True:
#         try:
#             data = queue.get()
#             print(data)
#         except KeyboardInterrupt:
#             pass