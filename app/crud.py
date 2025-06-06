from . import models, schemas
from sqlalchemy.orm import Session
from datetime import datetime

def create_trade(db: Session, trade: schemas.TradeCreate):
    db_trade = models.Trade(**trade.dict())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def get_trades(db: Session, ticker: str = None):
    query = db.query(models.Trade)
    if ticker:
        query = query.filter(models.Trade.ticker == ticker)
    return query.all()

def save_stock_average(db: Session, ticker: str, avg_price: float):
    avg_entry = models.StockAverage(
        ticker=ticker,
        average_price=avg_price,
        timestamp=datetime.utcnow()
    )
    db.add(avg_entry)
    db.commit()
