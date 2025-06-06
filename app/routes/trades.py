from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database
from typing import Optional
from datetime import datetime

router = APIRouter()

@router.post("/trades/", response_model=schemas.TradeResponse)
def add_trade(trade: schemas.TradeCreate, db: Session = Depends(database.get_session_local)):
    return crud.create_trade(db, trade)

@router.get("/trades/", response_model=list[schemas.TradeResponse])
def read_trades(
    ticker: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(database.get_session_local)
):
    return crud.get_trades(db, ticker=ticker, start_date=start_date, end_date=end_date)