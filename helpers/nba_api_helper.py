import pandas as pd
from nba_api.stats.endpoints import commonteamroster, playergamelog
from nba_api.stats.static import teams as nba_teams
from nba_api.stats.static import teams
from classes.teams import Team
from classes.players import Player
from helpers.retry_helper import retry_nba_call


"""
    Returns the team ID for a given team name.
    Handles the special cases for LA Clippers and LA Lakers.
"""
def get_team_id(team_name: str) -> int:
    if team_name in ["LA Clippers", "LA Lakers"]:
        # Convert to the full names used by the API
        full_name = "Los Angeles " + team_name.split()[1]
        return teams.find_teams_by_full_name(full_name)[0].get("id")
    return teams.find_teams_by_full_name(team_name)[0].get("id")


"""Fetch the raw roster and return a DataFrame with 
    ['PLAYER','PLAYER_ID'].
"""
def get_roster_df(team_id: int, season: str = "2024-25") -> pd.DataFrame:
    roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season)
    df = pd.DataFrame(roster.get_data_frames()[0])
    return df[["PLAYER", "PLAYER_ID"]]


def populate_team(team: Team):
    """
    Populates the Team object with its current players
    by extracting the roster and adding each player.
    """
    roster = get_roster_df(team)
    for player in roster.itertuples():
        # Note: Using player.PLAYER_ID and player.PLAYER to create the Player instance.
        team.add_player(Player(player.PLAYER_ID, player.PLAYER))

def safe_player_log(player_id, **opts):
    """
    Fetch a player's game log with automatic retries on connection errors.
    """
    return retry_nba_call(
        playergamelog.PlayerGameLog,
        player_id=player_id,
        **opts
    )

def safe_team_roster(team_id, **opts):
    """
    Fetch a team's roster with automatic retries on connection errors.
    Returns a DataFrame with ['PLAYER', 'PLAYER_ID'].
    """
    roster = retry_nba_call(
        commonteamroster.CommonTeamRoster,
        team_id=team_id,
        **opts
    )
    df = pd.DataFrame(roster.get_data_frames()[0])
    return df[["PLAYER", "PLAYER_ID"]]