#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()	#On attend le nom du client
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting) #On envoie la réponse
    print(f"> {greeting}")

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
