from database import SessionLocal
from helpers.nba_api_helper import *
from models.team_model import Team as TeamModel
from models.player_model import Player as PlayerModel

def load_team_and_roster(team_name) -> TeamModel:
    db = SessionLocal()

    try:
        #get the roster Dataframe
        roster_df = get_roster_df(get_team_id(team_name))
        nba_id = get_team_id(team_name)
        #check for existing row with nba_id
        team = (db.query(TeamModel).filter(TeamModel.nba_id == nba_id).first())
    
        if not team:
            team = TeamModel(
                nba_id = nba_id,
                name = team_name
            )
            db.add(team)
            db.commit()
            db.refresh(team)
    
        for row in roster_df.itertuples():
         player = (
                db.query(PlayerModel)
                  .filter(PlayerModel.nba_id == row.PLAYER_ID) #PLAYER_ID from DF
                  .first()
            )
         if not player:
                player = PlayerModel(
                    nba_id = row.PLAYER_ID,
                    name = row.PLAYER,
                    team_id = team.id 
                )
                db.add(player)
    
        db.commit()
        return team

    finally:
        db.close()
        