# api end points to remember
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/teamandplayersvsplayers.md

# common team roster
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamroster.md

# can view end points here
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints

#  View the outputs of end points
# https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints_output

# Get the player stats
# https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/playergamelog.md



# imports
from typing import List
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
from classes.games import Game
from classes.teams import Team
from classes.players import Player
import pandas as pd
import sys


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

        #Case that team is LA Clippers
        if t == "LA Clippers":
            return teams.find_teams_by_full_name(f'Los Angeles Clippers')[0].get("id")

        #Case that team is LA Lakers
        if t == "LA Lakers":
            return teams.find_teams_by_full_name(f'Los Angeles Lakers')[0].get("id")  

        return teams.find_teams_by_full_name(f'{t}')[0].get("id")

    def get_team_roster(t):
        #This returns more than one data frame: CommonTeamRoster and coaches
        team_info = commonteamroster.CommonTeamRoster(team_id=t, season="2024-25")
        return team_info
    
    
    #print_upcoming_games(get_games())

    ###########TESTING TO GET TEAM ROSTER

    print(get_team_id("Dallas Mavericks"))
    dallas = Team(get_team_id("Dallas Mavericks"), "Dallas Mavericks")
    x = get_team_roster(dallas.get_teamID())
    df = pd.DataFrame(x.get_data_frames()[0])
    roster = df[["PLAYER","PLAYER_ID"]]
    #print(roster)


    ### TESTING THE POPULATE A TEAM

    def populate(roster:pd.DataFrame, team:Team ):
        for player in roster.itertuples():
            name = player.PLAYER
            id = player.PLAYER_ID
            team.add_player(Player(id,name))
    
    def test_populate(team:Team):
        for player in team.get_players():
            print(player.get_playerName())
    
    populate(roster, dallas)
    test_populate(dallas)
    



    ###########TESTING THE LOAD TEAMS

"""""
 #   def load_team() -> List[Game]:
        today_games_dict = scoreboard.ScoreBoard().games.get_dict()
        games_today = []
        for games in today_games_dict:
                                        # New York   + Knicks                                  
            team1Name, team2Name = games["homeTeam"]["teamCity"] +" "+ games["homeTeam"]["teamName"], games["awayTeam"]["teamCity"]+" "+games["awayTeam"]["teamName"]
            team1ID, team2ID = get_team_id(team1Name), get_team_id(team2Name)
            game = Game(Team(team1ID,team1Name), Team(team2ID,team2Name))
            games_today.append(game)
        return games_today
    
 #   games = load_team()
    #[game, game2, game3, ...]
 #   for game in games:
        print(game.get_team1().get_teamName() + " vs "+ game.get_team2().get_teamName()) 
        print(str(game.get_team1().get_teamID()) + " vs "+ str(game.get_team2().get_teamID()))

 #   def load_players(team:Team):
        teamID = team.get_teamID


        pass

 #   def extract_players():
        pass

"""
    

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
sys.stdout.reconfigure(encoding='utf-8') #fix printing problem
get_team_players()

