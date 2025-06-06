import asyncio
import json
import random
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

import websockets

from sqlalchemy.orm import Session
from app.database import get_session_local
from app import crud

load_dotenv()

stocks = {"AAPL": 100.0, "GOOG": 150.0}
price_history = {ticker: [] for ticker in stocks}

async def simulate_price():
    uri = os.getenv("WEBSOCKET_URI")
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                while True:
                    ticker = random.choice(list(stocks.keys()))
                    price = round(random.uniform(100, 500), 2)
                    now = datetime.utcnow()
                    data = {
                        "ticker": ticker,
                        "price": price,
                        "timestamp": now.isoformat()
                    }

                    # Store price in history for 5-min average calculation
                    price_history[ticker].append((now, price))
                    # Keep only last 5 minutes of data
                    price_history[ticker] = [
                        (t, p) for (t, p) in price_history[ticker]
                        if t >= now - timedelta(minutes=5)
                    ]

                    await websocket.send(json.dumps(data))
                    print(f"[WebSocket] Sent {data}")
                    await asyncio.sleep(1)

        except Exception as e:
            print(f"[WebSocket] Connection error: {e}. Reconnecting in 5s...")
            await asyncio.sleep(5)

async def save_avg_prices():
    while True:
        async for db in get_session_local():
            for ticker in stocks:
                now = datetime.utcnow()
                five_min_ago = now - timedelta(minutes=5)
                prices = [p for t, p in price_history[ticker] if t >= five_min_ago]

                if prices:
                    avg_price = round(sum(prices) / len(prices), 2)
                    crud.save_stock_average(db, ticker, avg_price)
                    print(f"[DB] Saved 5-min average for {ticker}: {avg_price}")
        await asyncio.sleep(300)  # Wait 5 minutes
