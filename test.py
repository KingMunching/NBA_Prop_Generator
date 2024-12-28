# api end points to remember
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/teamandplayersvsplayers.md

# common team roster
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamroster.md


# can view end points here
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints


# imports
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd


def getRequest():
    # Basic Request
    # team_id = 1610612752 = New York Knicks
    team_info = commonteamroster.CommonTeamRoster(team_id=1610612752, season="2024-25")

    print(team_info.get_json())


def get_stats():
    # Function to fetch all game logs and filter for Christmas Day games
    def get_christmas_stats(player_id, season):
        # Fetch game logs for the player for the specified season
        player_logs = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        player_logs_df = player_logs.get_data_frames()[0]

        # Filter for games played on Christmas (December 25)
        player_logs_df['GAME_DATE'] = pd.to_datetime(player_logs_df['GAME_DATE'])
        christmas_stats = player_logs_df[player_logs_df['GAME_DATE'].dt.month == 12]
        christmas_stats = christmas_stats[christmas_stats['GAME_DATE'].dt.day == 25]

        return christmas_stats

    # Stephen Curry's Player ID and example usage
    player_id = 201939  # Stephen Curry's Player ID
    season = "2024-25"  # Adjust for the current season or any other season
    curry_christmas_stats = get_christmas_stats(player_id, season)

    # Display the filtered DataFrame
    print(curry_christmas_stats['PTS'])
    print(curry_christmas_stats['AST'])


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

    def get_team(t):
        return teams.find_teams_by_full_name(f'{t}')

    def get_team_id(t):
        return teams.find_teams_by_full_name(f'{t}')[0].get("id")

    def get_team_roster(t):
        team_info = commonteamroster.CommonTeamRoster(team_id=t, season="2024-25")
        return team_info

    upcoming_games = get_games()

    if upcoming_games:
        print("NBA Games:")
        for game in upcoming_games:
            # print(f'{game['Away Team']} vs {game['Home Team']}')
            print(get_team_id(game['Away Team']))
            print(get_team(game['Away Team']))
            print(get_team_id(game['Home Team']))
            print(get_team(game['Home Team']))


# run testing methods
getRequest()
get_stats()
get_team_players()

