from pydantic import BaseModel, validator
from datetime import datetime

class TradeBase(BaseModel):
    ticker: str
    price: float
    quantity: int
    side: str

    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

    @validator("quantity")
    def quantity_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Quantity must be positive")
        return v

    @validator("side")
    def side_must_be_buy_or_sell(cls, v):
        if v.upper() not in ("BUY", "SELL"):
            raise ValueError("Side must be BUY or SELL")
        return v.upper()

class TradeCreate(TradeBase):
    pass

class TradeResponse(TradeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True