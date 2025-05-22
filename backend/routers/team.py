from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from repositories.team_repository import TeamRepository
from repositories.player_repository import PlayerRepository
from service.game_service import get_teams_from_today_games
from schemas import TeamResponse, TeamCreate, PlayerResponse

router = APIRouter(
    prefix="/teams",
    tags=["teams"],
    responses={404: {"Description": "Not Found"}}
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all teams
@router.get("/", response_model=List[TeamResponse])
def get_teams(db: Session = Depends(get_db)):
    team_repo = TeamRepository(db)
    return team_repo.get_teams()

@router.get("/today", response_model=List[TeamResponse])
def get_today_teams(db: Session = Depends(get_db)):
    team_repo = TeamRepository(db)
    return get_teams_from_today_games(team_repo)

# Get team by team_id
@router.get("/{team_id}", response_model=TeamResponse)
def get_team(team_id:int,db: Session = Depends(get_db)):
    team_repo = TeamRepository(db)
    team = team_repo.get_team_by_id(team_id)
    if team:
        return team
    else:
        raise HTTPException(status_code=404, detail="Team not found")

# Get team's Key-Players
@router.get("/{team_id}/key-players", response_model=List[PlayerResponse])
def get_key_players(team_id: int, db: Session = Depends(get_db)):
    team_repo = TeamRepository(db)
    team = team_repo.get_team_by_id(team_id)
    if team:
        key_players = team_repo.get_key_players(team)
        return key_players
    else:
       raise HTTPException(status_code=404, detail="Team not found") 
