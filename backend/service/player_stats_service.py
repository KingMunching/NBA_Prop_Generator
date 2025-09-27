from database import SessionLocal
from models.player_stats import PlayerGameStat
from models.player_model import Player
from repositories.player_stats_repository import PlayerStatRepository


def load_last_n_games(player: Player, n: int = 20):
    db = SessionLocal()
    stats_repo = PlayerStatRepository(db)
    try:
        stats_repo.load_last_n_games(player, n)
        db.commit()
    finally:
        db.close()


def get_last_n_stats(player: Player, n: int):
    db = SessionLocal()
    stats_repo = PlayerStatRepository(db)
    try:
        # Use player.nba_id instead of player.id
        stats = stats_repo.get_last_n_stats(player.nba_id, n)
        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        db.close()
