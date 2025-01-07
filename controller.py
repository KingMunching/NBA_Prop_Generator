from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playercareerstats
from classes.games import Game

class controller:
    #list of game objects
    recent_games = []

    def __init__(self):
        pass
    
    # Get today's games
    def load_games():
        today_games_dict = scoreboard.ScoreBoard().__dict__
        games_today = []
        for games in today_games_dict:
            #create a new game object
            game = Game(games['homeTeam'], games['awayTeam'])
            games_today.append(game)
        return games_today
    
    def load_team_data():
        return None
    
    def load_player_data(self, player_id):
        return None


       