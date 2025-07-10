from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import PropResponse
from service.prop_service import PropGenerator
from models.team_model import Team

router = APIRouter(
    prefix="/props",
    tags=["props"],
    responses={404: {"Description": "Not Found"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/today")
async def generate_prop(request: PropResponse, db: Session = Depends(get_db)):
    #Testing teams. I would use get_today_teams if nba was live
    team1 = db.query(Team).filter(Team.name == "Los Angeles Lakers").first()

    team2 = db.query(Team).filter(Team.name == "Golden State Warriors").first()

    teams = [team1, team2]
    if not teams:
        return{"error": "No teams found in database"}
    
    prop_generator = PropGenerator(
        prop_type=request.prop_type,
        stat=request.stat,
        threshold=request.threshold,
        num_games=request.num_games,
        num_rec=request.num_rec
    )
    props = prop_generator.generate_daily_props(teams)
    return props

