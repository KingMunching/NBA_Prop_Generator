import time
from database import engine, Base, SessionLocal
import models           
from nba_api.stats.static import teams as nba_static
from service.team_service import load_team_and_roster
from models.player_model import Player
from service.player_stats_service import load_last_n_games
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    # this will create (or fetch) the DB row for Dallas, then insert its current roster
    #team = load_team_and_roster("Washington Wizards")



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

    """
    try:
        player = db.query(Player).first()
        #get stats of player
        recent_stats = player.stats.all()

        for stat in recent_stats:
            print(stat.date, stat.pts, stat.ast, stat.reb)
    finally:
        db.close() 
    """

    

    #Query all players
    players = db.query(Player).all()
    db.close() 
    #load stats
    for player in players:
        try:
            if player.stats.count() >= 20:
                continue
            load_last_n_games(player)
            print(f"Loaded stats for {player.name}")
        except Exception as e:
            print(f"Failed for {player.name}: {e}")
        time.sleep(0.2)

    