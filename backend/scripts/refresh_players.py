import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from nba_api.stats.static import teams as nba_teams
from database import SessionLocal
from models.player_model import Player
from helpers.nba_api_helper import  get_team_roster
from repositories.player_repository import PlayerRepository
from repositories.team_repository import TeamRepository
from models.team_model import Team

def refresh_team_players(team: Team, season = "2025-26"):
    db = SessionLocal()
    player_repo = PlayerRepository(db)

    print(f"refreshing roster for {team.name}")
    try:
        roster_df = get_team_roster(team.nba_id, season, safe=True)
        if roster_df.empty:
            print(f"roster_df for {team.name} is empty")
            return
        api_player_ids = set(roster_df["PLAYER_ID"])
    except Exception as e:
        print(f"Error fetching roster for {team.name}: {e}")
        db.close()
        return 

    #fetch current players in that roster from db
    db_players = player_repo.get_players_by_team_id(team.nba_id)
    db_player_map = {}
    for player in db_players:
        db_player_map[player.nba_id] = player
    
    #process the players
    for _, row in roster_df.iterrows():
        player_id = row["PLAYER_ID"]
        player_name = row["PLAYER"]

        if player_id not in db_player_map:
           #if player is new to the team then check if they exist at all
           existing_player = player_repo.get_player_by_nba_id(player_id)

           if existing_player:
               print(f"updating {player_name} to team {team.name}")
               existing_player.team_nba_id = team.nba_id 
           else:
               new_player = Player(
                   nba_id = player_id,
                   player_name = player_name,
                   team_nba_id = team.nba_id
               )
               db.add(new_player)
    
    for player_id, player in db_player_map.items():
        if player_id not in api_player_ids:
            print(f"{player.player_name} is no longer pn {team.name}")
            player.team_nba_id = None
    
    db.commit()
    db.close()
    print(f"finished refreshing rosters for {team.name}")

if __name__ == "__main__":
    refresh_players()