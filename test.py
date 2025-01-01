# api end points to remember
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/teamandplayersvsplayers.md

# common team roster
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamroster.md


# can view end points here
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints

#  View the outputs of end points
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints_output


# imports
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd


def getRequest():
    # Basic Request
    # team_id = 1610612752 = New York Knicks
    team_info = commonteamroster.CommonTeamRoster(team_id=1610612752, season="2024-25")

    print(team_info.get_json())


def get_team_players():
    
    def get_games():
        # Fetch data for all games schedule for today
        today_games = scoreboard.ScoreBoard()
        games_data = today_games.games.get_dict()

        upcoming_games = []
        for game in games_data:
            home_team = game['homeTeam']['teamName']
            away_team = game['awayTeam']['teamName']

            upcoming_games.append({
                'Home Team': home_team,
                'Away Team': away_team
            })
        return upcoming_games
    
    #for testing purposes
    def print_upcoming_games(upcoming_games):
        if upcoming_games:
            print("NBA Games:")
        for game in upcoming_games:
            print(f'{game['Away Team']} vs {game['Home Team']}')

    def get_team(t):
        return teams.find_teams_by_full_name(f'{t}')

    def get_team_id(t):
        return teams.find_teams_by_full_name(f'{t}')[0].get("id")

    def get_team_roster(t):
        team_info = commonteamroster.CommonTeamRoster(team_id=t, season="2024-25")
        return team_info
    
    print_upcoming_games(get_games())

#    upcoming_games = get_games()
#    if upcoming_games:
#        print("NBA Games:")
#        for game in upcoming_games:
#            # print(f'{game['Away Team']} vs {game['Home Team']}')
#            print(get_team_id(game['Away Team']))
#            print(get_team(game['Away Team']))
#            print(get_team_id(game['Home Team']))
#            print(get_team(game['Home Team']))


def get_player_stats(id):
    career = playercareerstats.PlayerCareerStats(player_id=id)
    return career


# run testing methods
# getRequest()
# get_stats()
get_team_players()

# get player stats from last N games
