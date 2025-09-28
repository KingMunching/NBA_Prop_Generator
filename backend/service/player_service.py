from nba_api.stats.endpoints import playercareerstats
from models.player_model import Player
from database import SessionLocal

def get_player_stats(player_id):
    """
    Retrieves the career stats for a given player by using the player ID.
    Returns the object provided by the NBA API.
    """
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    return career


def load_player_stats(player):
    
    pass

def get_player_by_name(name):
    db = SessionLocal()
    try:
        player = db.query(Player).filter(Player.player_name == name).first()
        return player
    finally:
        db.close()
        
    