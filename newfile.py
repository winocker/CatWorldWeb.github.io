import asyncio
import websockets

USERS = set()

async def addUser(websocket):
    USERS.add(websocket)

async def removeUser(websocket):
    USERS.remove(websocket)

async def socket(websocket, path):
    await addUser(websocket)
    print(len(USERS), USERS)	
async def socket(websocket, path):
    print(websocket, path)

    try:
        while True:
            message = await websocket.recv()
            
            await asyncio.wait([user.send(message) for user in USERS])
    finally:
        await removeUser(websocket)
start_server = websockets.serve(socket, '127.0.0.1', 5699)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()