from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

@router.post("/trades/", response_model=schemas.TradeResponse)
def add_trade(trade: schemas.TradeCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_trade(db, trade)

@router.get("/trades/", response_model=list[schemas.TradeResponse])
def read_trades(ticker: str = None, db: Session = Depends(database.SessionLocal)):
    return crud.get_trades(db, ticker)
