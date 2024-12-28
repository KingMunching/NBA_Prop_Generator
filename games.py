from nba_api.live.nba.endpoints import scoreboard

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

upcoming_games = get_games()

if upcoming_games:
    print("NBA Games:")
    for game in upcoming_games:
        print(f'{game['Away Team']} vs {game['Home Team']}')