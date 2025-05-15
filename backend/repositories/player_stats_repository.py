from sqlalchemy.orm import Session
from models.player_stats import PlayerGameStat
from models.player_model import Player
from helpers.nba_api_helper import safe_player_log
from datetime import datetime

class PlayerStatRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def get_last_n_stats(self, player_id: int, n: int):
        stats = self.db.query(PlayerGameStat) \
                      .filter_by(player_id=player_id) \
                      .order_by(PlayerGameStat.date.desc()) \
                      .limit(n) \
                      .all()
        return stats
    
    def load_last_n_games(self, player: Player, n:int = 20):
        #Get player stats from nba api
        log = safe_player_log(
                player_id = player.nba_id,
                season= "2024-25",
                season_type_all_star="Regular Season"
            )
        df = log.get_data_frames()[0]
        #Get last 20 games stats
        recent = df.head(20)

        for row in recent.itertuples():
            date = datetime.strptime(row.GAME_DATE, "%b %d, %Y").date()
                
            #Check if game stats for date exist
            exist = (
                self.db.query(PlayerGameStat).filter_by(player_id = player.id, date=date).first()
                )
            #if stat in db, continue on to next row
            if exist:
                continue
                
            stat = PlayerGameStat(
                    player_id = player.id,
                    date      = date,
                    pts       = row.PTS,
                    ast       = row.AST,
                    reb       = row.REB,
                    stl       = row.STL,
                    blk       = row.BLK,
                    tov       = row.TOV,
                    min       = row.MIN
                )
            self.db.add(stat)
        self.db.commit()
        