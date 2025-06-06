from fastapi import APIRouter, Query
from aws_lambda.lambda_function import lambda_handler

router = APIRouter()

@router.post("/lambda/run")
def run_lambda(date: str = Query(None, description="Date in YYYY-MM-DD format")):
    event = {"date": date} if date else {}
    response = lambda_handler(event, None)
    return response
