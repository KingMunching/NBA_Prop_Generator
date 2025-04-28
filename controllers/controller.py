from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
from classes.games import Game
from classes.teams import Team
from classes.players import Player

class controller:
    #list of game objects
    recent_games = []

    def __init__(self):
        pass

    def get_team_id(self, t):
        return teams.find_teams_by_full_name(f'{t}')[0].get("id")
    
    # Get today's games
    def load_games(self):
        today_games_dict = scoreboard.ScoreBoard().__dict__
        games_today = []
        for games in today_games_dict:
                                        # New York   + Knicks                                  
            team1Name, team2Name = games["homeTeam"]["teamCity"] 
            +" "+ games["homeTeam"]["teamName"], 
            games["awayTeam"]["teamCity"]
            +" "+games["awayTeam"]["teamName"]
            team1ID, team2ID = self.get_team_id(team1Name), self.get_team_id(team2Name)
            game = Game(Team(team1ID,team1Name), Team(team2ID,team2Name))
            games_today.append(game)
        return games_today
    
    def load_players_in_team(self, team:Team):
            team.set_players()
            pass
    
    def load_player_data(self, player_id):
        return None
    

       