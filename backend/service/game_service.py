from typing import List
from nba_api.live.nba.endpoints import scoreboard
from models.team_model import Team
from repositories.team_repository import TeamRepository
from database import SessionLocal
from redis_client import redis_client
import json
from datetime import datetime, timezone



"""
    Fetches all games scheduled for today and returns a list of dictionaries 
    containing the home and away team names.
    """

def get_teams_from_today_games(team_repo: TeamRepository) -> List[Team]:

    date_today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cache_key = f"teams_today: {date_today_str}"
    cached_team_names = redis_client.get(cache_key)

    team_names = set()

    
    if cached_team_names:
       print("cache hit for teams today")
       team_names = set(json.loads(cached_team_names))
    else:
        print("cache miss for fetch todays games")
        today_games = scoreboard.ScoreBoard()
        games_data = today_games.games.get_dict()

        for game in games_data:
            home_team = f"{game['homeTeam']['teamCity']} {game['homeTeam']['teamName']}"
            away_team = f"{game['awayTeam']['teamCity']} {game['awayTeam']['teamName']}"
    
            home_team_from_db = team_repo.get_team_by_name(home_team)
            away_team_from_db = team_repo.get_team_by_name(away_team)
   
            if home_team_from_db is not None:
                team_names.add(home_team_from_db.name)
   
            if away_team_from_db is not None:
                team_names.add(away_team_from_db.name)

        redis_client.set(cache_key, json.dumps(list(team_names)), ex=28800)

    teams = set()
    for name in team_names:
        team_from_db = team_repo.get_team_by_name(name)
        if team_from_db:
            teams.add(team_from_db)
    
    return list(teams)


def print_upcoming_games(upcoming_games):
    """Prints the list of upcoming NBA games."""
    if upcoming_games:
        print("NBA Games:")
    for game in upcoming_games:
        print(f"{game['Away Team']} vs {game['Home Team']}")

