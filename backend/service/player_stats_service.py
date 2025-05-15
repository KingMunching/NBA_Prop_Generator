from database import SessionLocal
from nba_api.stats.endpoints import playergamelog
from models.player_stats import PlayerGameStat
from models.player_model import Player
from datetime import datetime
from helpers.nba_api_helper import safe_player_log
from repositories.player_stats_repository import PlayerStatRepository


def load_last_n_games(player: Player, n:int = 20):
    db = SessionLocal()
    stats_repo = PlayerStatRepository(db)
    try:
        stats_repo.load_last_n_games(player, n)
        db.commit()
    finally:
        db.close()


def get_last_n_stats(player: Player, n :int):
    db = SessionLocal()
    stats_repo = PlayerStatRepository(db)
    try:
        stats = stats_repo.get_last_n_stats(player.id, n)
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        db.close() 
        

    