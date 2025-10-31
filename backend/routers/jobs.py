import time 
from fastapi import APIRouter, Depends, HTTPException, Request, status, BackgroundTasks
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

def run_update_logic(db: Session):
    team_repo = TeamRepository(db)
    teams = get_teams_from_today_games(team_repo)
   
    print(f"BACKGROUND JOB: Found {len(teams)} teams to update.")
   
    for team in teams:
        print(f"BACKGROUND JOB: Updating stats for team: {team.name}")
        update_team_stats(db, team)
        time.sleep(15)
   
    print("BACKGROUND JOB: Finished updating all team stats.")


CRON_SECRET_KEY = os.getenv("CRON_SECRET_KEY")
@router.post("/update-today-stats")
async def update_today_stats(request: Request,background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    auth_header = request.headers.get("Authorization")
    # the endpoint must be accessed with a secret key
    if not CRON_SECRET_KEY or auth_header != f"Bearer {CRON_SECRET_KEY}":
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Invalid or missing AUTH token"
        )
    
    background_tasks.add_task(run_update_logic, db)

    return {"status": "success", "message": "Accepted: Stat update job started in the background."}
    


