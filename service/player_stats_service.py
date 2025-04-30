from database import SessionLocal
from nba_api.stats.endpoints import playergamelog
from models.player_stats import PlayerGameStat
from models.player_model import Player
from datetime import datetime

def load_last_n_games(player: Player):
    db = SessionLocal()
    try:
        #Get player stats from nba api
        log = playergamelog.PlayerGameLog(
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

# Return player stats. Last 20 stats
def get_player_stats_by_nba_id(nba_id:int):
    db = SessionLocal

    try:
        player = db.query(Player).filter_by(nba_id=nba_id).first()

        if player:
            recent_stats = player.stats.all()
            return recent_stats
        else:
            return None
    finally:
        db.close()