from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base
from datetime import datetime

class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    side = Column(String)  # BUY/SELL
    timestamp = Column(DateTime, default=datetime.utcnow)

class StockAverage(Base):
    __tablename__ = "stock_averages"
    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    average_price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
