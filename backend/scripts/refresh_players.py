import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pandas as pd
from nba_api.stats.static import teams as nba_teams
from database import SessionLocal
from models.player_model import Player
from helpers.nba_api_helper import  get_team_roster
from repositories.player_repository import PlayerRepository




def refresh_players(season ="2025-26"):
    db = SessionLocal()
    repo = PlayerRepository(db)

    all_teams = nba_teams.get_teams()

    for team in all_teams:
        team_id = team['id']
        team_name = team['full_name']

        print(f"Getting Roster for {team_name} - {season}")
        roster_df = get_team_roster(team_id, season=season, safe=True)   
        
        for _, row in roster_df.iterrows():
            db_player = repo.get_player_by_nba_id(row["PLAYER_ID"])

            if db_player:
                #update existing plater
                db_player.name = row['PLAYER']
                db_player.team_nba_id = team_id
            else:
                #new player
                player = Player(
                    nba_id = row['PLAYER_ID'],
                    name = row['PLAYER'],
                    team_nba_id = team_id
                )
                db.add(player)
                print(f"🆕 Inserted new player: {row['PLAYER']} ({row['PLAYER_ID']}) for {team_name}")

        db.commit()
    
    db.close()
    print("Done updating")

if __name__ == "__main__":
    refresh_players()