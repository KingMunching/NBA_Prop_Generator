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
from nba_api.stats.static import players

if __name__ == "__main__":

   db = SessionLocal()
   
   for player in db.query(Player).all():
      print(f"printed stats for {player.player_name}")
      load_last_n_games(player, n=20)

   print("finished")

