from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.static import players


def get_games():
    #Fetch data for all games schedule for today
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
        print(get_team_id(game['Home Team']))
