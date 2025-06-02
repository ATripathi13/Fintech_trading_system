from . import models, schemas
from sqlalchemy.orm import Session

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
