from fastapi import APIRouter

from algo_trading.moving_average import run_strategy

router = APIRouter()

@router.post("/strategy/moving_average")
def moving_average_strategy():
    result = run_strategy()
    return result
