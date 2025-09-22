import uvicorn
from fastapi import FastAPI
from database import engine, Base, SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from routers import team, player, props

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5175",

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

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the NBA Prop Bet Analytics API",
        "docs_url": "/docs",
        "api_version": "1.0.0"
    }


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)