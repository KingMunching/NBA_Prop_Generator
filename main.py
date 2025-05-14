import time
from database import engine, Base, SessionLocal
import models           
from service.prop_service import PropGenerator
from service.team_service import load_team_and_roster
from models.player_model import Player
from service.player_stats_service import load_last_n_games, get_last_n_stats
from nba_api.stats.static import teams
from service.player_service import get_player_by_name
from repositories.player_repository import PlayerRepository
from repositories.team_repository import TeamRepository
from service.game_service import get_teams_from_today_games
    
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    # this will create (or fetch) the DB row for Dallas, then insert its current roster
    #team = load_team_and_roster("Washington Wizards")
    generator = PropGenerator(
        prop_type="pts",
        stat=20,                  # Threshold value (e.g., 15 points)
        num_games=20,
        num_rec=10,
        threshold=0.5      # Minimum success rate of 80%
    )

    # Load teams and players (example)
    teams_today = get_teams_from_today_games()
    props = generator.generate_daily_props(teams_today)
    

    # Print results
    for prop in props:
       print(f"{prop['player_name']}: {prop['success_rate']:.2%} success rate")
    
    """
    #Query all players
    db = SessionLocal()
    player_repo = PlayerRepository(db)
    players = player_repo.get_players()
    #print(len(players))
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
    """
    

