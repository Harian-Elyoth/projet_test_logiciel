#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")	#On affiche la question puis on attend que l'utilisateur rentre un nom

        await websocket.send(name)		#On envoie le nom
        print(f"> {name}")				#On affiche ce nom

        greeting = await websocket.recv()	#On attend la réponse du serveur
        print(f"< {greeting}")			#On affiche cette réponse

while(1):

	asyncio.get_event_loop().run_until_complete(hello())	#On appelle la fonction hello et on attend qu'elle se termine
