from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from schemas import PropResponse, PropGeneratedResponse, PropCreate, PropSavedResponse, UserPropsResponse, PropRequestBase
from service.prop_service import PropGenerator
from models.team_model import Team
from uuid import UUID
from service import prop_service
from auth.dependencies import get_current_user
from service.game_service import get_teams_from_today_games
from repositories.team_repository import TeamRepository
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
 
@router.get("/", response_model=UserPropsResponse)
async def get_user_props(db: Session = Depends(get_db),
                        user_id: str=Depends(get_current_user)):
    props = prop_service.get_props_by_user(db, user_id)
    return {"props": props}

#Save props
@router.post("/save", response_model=PropSavedResponse)
async def save_prop(prop: PropCreate, 
                    db: Session = Depends(get_db), 
                    user_id: str = Depends(get_current_user)):
    return prop_service.create_prop(db, prop, user_id)

@router.delete("/delete/{prop_id}")
async def delete_prop(prop_id: UUID,
                      db: Session = Depends(get_db), 
                      user_id: str = Depends(get_current_user)):
    
    prop_service.delete_prop(db, user_id, prop_id)

@router.post("/today", response_model=List[PropGeneratedResponse])
async def generate_prop(request: PropRequestBase, db: Session = Depends(get_db)):
      
    team_repo = TeamRepository(db)
    teams = get_teams_from_today_games(team_repo)
    team_with_none = []

    for team in teams:
        if team is not None:
            team_with_none.append(team)

    
    #if not teams:
    #   return{"error": "No teams found in database"}
    
    prop_generator = PropGenerator(
        prop_type=request.prop_type,
        stat=request.stat,
        threshold=request.threshold,
        num_games=request.num_games,
        num_rec=request.num_rec,
        z_score_threshold = request.z_score_threshold
    )
    props = prop_generator.generate_daily_props(teams)
    return props

