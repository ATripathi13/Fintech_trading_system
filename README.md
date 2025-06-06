# Fintech Trading System #
A real-time trading platform built with FastAPI, PostgreSQL, WebSockets, and AWS (S3/Lambda), designed for:

* Real-time stock price simulation

* Trade & analytics APIs

* Algorithmic trading (optional)

* CSV import, scheduled tasks

* Secure WebSocket communication

## Features ##
* REST APIs (FastAPI + Swagger UI)

* Real-time WebSocket server (websockets module)

* Moving average trading logic (optional strategy module)

* AWS Lambda + S3 integration for batch analytics

* Periodic 5-minute average stock price tracking

* Async PostgreSQL session with SQLAlchemy

## Project Structure ##

.
├── app/

│   ├── main.py              # FastAPI app entry

│   ├── crud.py              # DB interaction functions

│   ├── models.py            # SQLAlchemy models

│   ├── database.py          # DB session + engine

│   └── schemas.py           # Pydantic schemas

├── websocket/

│   └── server.py            # WebSocket server logic

├── run.py                   # Launches FastAPI + WebSocket server

├── .env                     # Environment variables

├── requirements.txt

└── README.md

## Installation & Setup ##

#### 1. Clone & create virtual environment ####

* git clone https://github.com/your-username/fintech-trading-system.git
* cd fintech-trading-system
* python -m venv myenv
* source myenv/bin/activate  # or `myenv\Scripts\activate` on Windows

#### 2. Install dependencies ####

* pip install -r requirements.txt

#### 3. Set up .env ####

* Create a .env file in the root:

    APP_HOST=127.0.0.1
    APP_PORT=8000
    WEBSOCKET_URL=ws://localhost:8765
    DATABASE_URL=postgresql://user:password@localhost:5432/yourdb


## Run Locally ##

Option 1: Run WebSocket only

    python websocket/server.py and uvicorn main:app --reload separately

Option 2: Run FastAPI + WebSocket together

    python run.py (recommended)

## API Docs ##

Once the FastAPI server is running:

* Swagger UI: http://localhost:8000/docs

* ReDoc: http://localhost:8000/redoc


### Assumptions ###

* For the trade analysis and websocket two trades initial amount AAPL = 100 and GOOG = 150
* For the optional trading initial amount = 1000