import asyncio
import websockets

connected_clients = set()

async def handler(websocket):
    print("Client connected")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            for client in connected_clients.copy():
                if not client.closed:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.remove(websocket)

async def start_websocket_server():
    server = await websockets.serve(handler, "localhost", 8765)
    print("WebSocket server started on ws://localhost:8765")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_websocket_server())
