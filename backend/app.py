import uvicorn
from fastapi import FastAPI
from database import engine, Base, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from routers import team, player, props, jobs

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5175",
    "http://172.18.0.3:5173"
    "https://nba-prop-generator.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*'],
    )

app.include_router(team.router)
app.include_router(player.router)
app.include_router(props.router)
app.include_router(jobs.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the NBA Prop Bet Analytics API",
        "docs_url": "/docs",
        "api_version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return{"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)