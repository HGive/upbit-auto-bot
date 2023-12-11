import websockets
import json
import asyncio

async def subscribe(ticker,uri, queue):
    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket": "test"},
            {
                "type": "ticker",
                "codes": [ticker]
            },
        ]
        await websocket.send(json.dumps(subscribe_fmt))
        while True:
            response = await websocket.recv()
            await queue.put(response)


async def main(ticker,main_queue):
    data_queue = asyncio.Queue()
    subscribe_task = asyncio.create_task(subscribe(ticker,"wss://api.upbit.com/websocket/v1",data_queue))
    while True:
        data = await data_queue.get()
        await main_queue.put(data)