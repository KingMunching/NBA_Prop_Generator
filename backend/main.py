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
from helpers.nba_api_helper import get_roster_df

if __name__ == "__main__":
   print(get_roster_df(1610612742))

    

