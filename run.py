import os
from dotenv import load_dotenv
import asyncio
import uvicorn
from websocket.server import start_websocket_server  # adjust import if needed

load_dotenv()

async def main():
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", 8000))

    config = uvicorn.Config("app.main:app", host=host, port=port, reload=True)
    server = uvicorn.Server(config)

    await asyncio.gather(
        server.serve(),
        start_websocket_server()
    )

if __name__ == "__main__":
    asyncio.run(main())
