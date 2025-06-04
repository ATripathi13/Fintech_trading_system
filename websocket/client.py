import asyncio
import random
from datetime import datetime, timedelta

stocks = {"AAPL": 100.0, "GOOG": 150.0}

async def simulate_price():
    stock_prices = {ticker: [price] for ticker, price in stocks.items()}
    start_time = datetime.utcnow()

    while True:
        for ticker in stocks:
            change = random.uniform(-0.5, 0.5)
            new_price = round(stocks[ticker] * (1 + change / 100), 2)
            stock_prices[ticker].append(new_price)
            stocks[ticker] = new_price

            # Log notification if >2% increase in 1 minute
            if datetime.utcnow() - start_time >= timedelta(minutes=1):
                prices = stock_prices[ticker][-60:]
                if prices[0] and (new_price - prices[0]) / prices[0] > 0.02:
                    print(f"🚨 {ticker} price increased >2% in 1 minute!")

        await asyncio.sleep(1)

asyncio.run(simulate_price())
