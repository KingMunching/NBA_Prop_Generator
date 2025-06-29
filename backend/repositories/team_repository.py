from typing import List
from sqlalchemy.orm import Session
from models.team_model import Team as TeamModel
from models.player_model import Player as PlayerModel
from models.player_stats import PlayerGameStat
from sqlalchemy import func, cast, Integer

class TeamRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_teams(self):
        return self.db.query(TeamModel).all()
    
    def get_team_by_id(self, team_id: int):
        return self.db.query(TeamModel).filter(TeamModel.id == team_id).first()
    
    def get_team_by_name(self, team_name: str):
        return self.db.query(TeamModel).filter(TeamModel.name == team_name).first()
    
    def get_team_by_nba_id(self, nba_id: int):
        return self.db.query(TeamModel).filter(TeamModel.nba_id == nba_id).first()
    
    def create_team(self, team: TeamModel):
        self.db.add(team)
        self.db.commit()
        self.db.refresh(team)
        return team

    def delete_team(self, team_id: int):
        db_team = self.db.query(TeamModel).filter(TeamModel.id == team_id).first()
        if db_team:
            self.db.delete(db_team)
            self.db.commit()
        return db_team
    
    def get_key_players(self, team: TeamModel) -> List[PlayerModel]:
        #Get players in team
        players = (self.db.query(PlayerModel, func.sum(cast(PlayerGameStat.min, Integer)).label("total_min"))
        .join(PlayerGameStat, PlayerModel.id == PlayerGameStat.player_id)\
        .filter(PlayerModel.team_id == team.id).group_by(PlayerModel.id)\
        .order_by(func.sum(cast(PlayerGameStat.min, Integer)).desc())
        .limit(3).all()
        )

        key_players = []
        for player, total_min in players:
            key_players.append(player)
        return key_players

