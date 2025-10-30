import time 
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
import os
from database import SessionLocal
from repositories.team_repository import TeamRepository
from service.game_service import get_teams_from_today_games
from scripts.update_stats import update_team_stats

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix='/jobs',
    tags=['jobs']
)

CRON_SECRET_KEY = os.getenv("CRON_SECRET_KEY")
router.post("/update-today-stats")
async def update_today_stats(request: Request, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    # the endpoint must be accessed with a secret key
    if not CRON_SECRET_KEY or auth_header != f"Bearer {CRON_SECRET_KEY}":
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid or missing AUTH token"
        )
    
    team_repo = TeamRepository(db)
    teams = get_teams_from_today_games(team_repo)

    print(f"Found {len(teams)} to update")

    for team in teams:
        update_team_stats(team)
        time.sleep(15)
    
    return {"status": "success", "message": f"Updated stats for {len(teams)} teams."}


