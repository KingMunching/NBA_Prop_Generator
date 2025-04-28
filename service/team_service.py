from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
import pandas as pd
from classes.teams import Team
from classes.players import Player

def get_team_roster(team_id, season="2024-25"):
    """Fetches the team roster for a given team_id and season."""
    return commonteamroster.CommonTeamRoster(team_id=team_id, season=season)

def extract_roster(team: Team) -> pd.DataFrame:
    """
    Converts a team’s roster information to a DataFrame and returns
    only the player names and their IDs.
    """
    roster = get_team_roster(team.get_teamID())
    df = pd.DataFrame(roster.get_data_frames()[0])
    return df[["PLAYER", "PLAYER_ID"]]

def populate_team(team: Team):
    """
    Populates the Team object with its current players
    by extracting the roster and adding each player.
    """
    roster = extract_roster(team)
    for player in roster.itertuples():
        # Note: Using player.PLAYER_ID and player.PLAYER to create the Player instance.
        team.add_player(Player(player.PLAYER_ID, player.PLAYER))

def test_populate_team(team: Team):
    """
    Iterates through the players stored in the team and prints their names and IDs.
    """
    for player in team.get_players():
        print(f"{player.get_playerName()}, {player.get_playerID()}")

def get_team_id(team_name: str) -> int:
    """
    Returns the team ID for a given team name.
    Handles the special cases for LA Clippers and LA Lakers.
    """
    if team_name in ["LA Clippers", "LA Lakers"]:
        # Convert to the full names used by the API
        full_name = "Los Angeles " + team_name.split()[1]
        return teams.find_teams_by_full_name(full_name)[0].get("id")
    return teams.find_teams_by_full_name(team_name)[0].get("id")
