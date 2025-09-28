from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
from repositories.player_repository import PlayerRepository
from service.player_stats_service import load_last_n_games, get_last_n_stats
from schemas import PlayerResponse, PlayerCreate, PlayerWithStats, PlayerGameStatResponse

router = APIRouter(
    prefix="/players",
    tags=["players"],
    responses={404: {"Description": "Not Found"}}
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    player_repo = PlayerRepository(db)
    return player_repo.get_players()

@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id:int, db: Session = Depends(get_db)):
    player_repo = PlayerRepository(db)
    player = player_repo.get_player_by_nba_id(player_id)
    if player:
        return player
    else:
        raise HTTPException(status_code=404, detail="Player not found")
    
@router.get("/{player_id}/stats", response_model=List[PlayerGameStatResponse])
def get_player_stats(player_id: int, num_games: int = 10, db: Session = Depends(get_db)):
    player_repo = PlayerRepository(db)
    player = player_repo.get_player_by_id(player_id)
    if player:
        stats = get_last_n_stats(player, num_games)
        return stats
    else:
        raise HTTPException(status_code=404, detail="Player not found")