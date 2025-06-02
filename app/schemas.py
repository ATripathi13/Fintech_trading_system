from pydantic import BaseModel
from datetime import datetime

class TradeBase(BaseModel):
    ticker: str
    price: float
    quantity: int
    side: str

class TradeCreate(TradeBase):
    pass

class TradeResponse(TradeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
