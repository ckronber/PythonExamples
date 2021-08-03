#!/usr/bin/env python

# WS client example
# None of this code is mine

import asyncio
import websockets

while(1):
    async def hello():
        uri = "ws://localhost:8765"

        async with websockets.connect(uri) as websocket:
            name = input("What's your name? ")

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

    asyncio.get_event_loop().run_until_complete(hello())