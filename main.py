from classes.teams import Team
from service.team_service import *
from service.game_service import *
from service.player_service import *
import sys

def main():
    
    # Example: Working with a team
    mavericks_id = get_team_id("Dallas Mavericks")
    dallas = Team(mavericks_id, "Dallas Mavericks")
    populate_team(dallas)
    test_populate_team(dallas)
    
    # Example: Working with games
    games = get_games()
    print_upcoming_games(games)
    
    # Example: Get player stats (replace player_id with an actual ID)
    # stats = get_player_stats(player_id)
    # print(stats.get_json())  # Uncomment and adjust when using a valid player ID

if __name__ == "__main__":
    main()
