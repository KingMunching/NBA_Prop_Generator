from database import SessionLocal
from helpers.nba_api_helper import *
from models.team_model import Team as TeamModel
from models.player_model import Player as PlayerModel
from repositories.team_repository import TeamRepository
from repositories.player_repository import PlayerRepository

def load_team_and_roster(team_name) -> TeamModel:
    db = SessionLocal()
    team_repo = TeamRepository(db)
    player_repo = PlayerRepository(db)

    try:
        #get the roster Dataframe
        roster_df = safe_team_roster(get_team_id(team_name))
        nba_id = get_team_id(team_name)
        #check for existing row with nba_id
        team = team_repo.get_team_by_nba_id(nba_id)
    
        if not team:
            team = TeamModel(
                nba_id = nba_id,
                name = team_name
            )
            #Add to db
            team_repo.create_team(team)
    
        for row in roster_df.itertuples():
            player = player_repo.get_player_by_nba_id(row.PLAYER_ID)
            if not player:
                player = PlayerModel(
                    nba_id = row.PLAYER_ID,
                    name = row.PLAYER,
                    team_id = team.id 
                )
                player_repo.create_player(player)
        db.commit()
        return team

    finally:
        db.close()
        