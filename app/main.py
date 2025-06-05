from fastapi import FastAPI
from dotenv import load_dotenv
import os
from .routes import trades

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI App"))
app.include_router(trades.router)





