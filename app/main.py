from fastapi import FastAPI
from .routes import trades

app = FastAPI()
app.include_router(trades.router)
