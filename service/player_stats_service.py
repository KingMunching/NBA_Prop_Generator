from database import SessionLocal
from nba_api.stats.endpoints import playergamelog
from models.player_stats import PlayerGameStat
from models.player_model import Player
from datetime import datetime
from helpers.nba_api_helper import safe_player_log


def load_last_n_games(player: Player):
    db = SessionLocal()
    try:
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
            
            #Check if player in db
            exist = (
                db.query(PlayerGameStat).filter_by(player_id = player.id).first()
            )
            #if player in db, continue on to next row
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
                tov       = row.TOV
            )
            db.add(stat)
        db.commit()
    finally:
        db.close()
