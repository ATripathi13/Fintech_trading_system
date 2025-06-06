from fastapi import FastAPI
from dotenv import load_dotenv
import os
import asyncio

from app.routes import trades, analysis, lambda_runner
from app.database import init_db
from websocket.client import simulate_price  

load_dotenv()
init_db()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))

app.include_router(trades.router)
app.include_router(analysis.router)
app.include_router(lambda_runner.router)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(simulate_price())
