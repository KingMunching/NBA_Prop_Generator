from typing import List
from nba_api.live.nba.endpoints import scoreboard
from models.team_model import Team
from repositories.team_repository import TeamRepository
from database import SessionLocal

"""
    Fetches all games scheduled for today and returns a list of dictionaries 
    containing the home and away team names.
    """

def get_teams_from_today_games(team_repo: TeamRepository) -> List[Team]:
    today_games = scoreboard.ScoreBoard()
    games_data = today_games.games.get_dict()

    teams = set()
    for game in games_data:
        home_team = f"{game['homeTeam']['teamCity']} {game['homeTeam']['teamName']}"
        away_team = f"{game['awayTeam']['teamCity']} {game['awayTeam']['teamName']}"
        
        home_team_from_db = team_repo.get_team_by_name(home_team)
        away_team_from_db = team_repo.get_team_by_name(away_team)

        teams.add(home_team_from_db)
        teams.add(away_team_from_db)

    return list(teams)


def print_upcoming_games(upcoming_games):
    """Prints the list of upcoming NBA games."""
    if upcoming_games:
        print("NBA Games:")
    for game in upcoming_games:
        print(f"{game['Away Team']} vs {game['Home Team']}")

