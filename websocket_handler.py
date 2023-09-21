import websockets
import json

async def subscribe(uri, handler):
    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket": "test"},
            {
                "type": "ticker",
                "codes": ["KRW-BTC"],
                "isOnlySnapshot": False,
            },
        ]
        await websocket.send(json.dumps(subscribe_fmt))
        while True:
            response = await websocket.recv()
            handler(response)

def handler(response):
    print(response)

async def main():
    await subscribe("wss://api.upbit.com/websocket/v1", handler)