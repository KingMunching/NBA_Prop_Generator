from database import engine, Base, SessionLocal
import models           
from service.team_service import load_team_and_roster
from models.player_model import Player
from service.player_stats_service import load_last_n_games, get_player_stats_by_nba_id
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    # this will create (or fetch) the DB row for Dallas, then insert its current roster
    #team = load_team_and_roster("Dallas Mavericks")
    
    db = SessionLocal()

    """
    try:
        player = db.query(Player).first()
        if not player:
            print("No player found with that NBA ID.")
        load_last_n_games(player)
        print(f"Stored last 20 games for {player.name} (NBA ID {player.nba_id}).")
    finally:
        db.close()
    """

    try:
        player = db.query(Player).first()
        recent_stats = player.stats.all()

        for stat in recent_stats:
            print(stat.date, stat.pts, stat.ast, stat.reb)
    finally:
        db.close() 