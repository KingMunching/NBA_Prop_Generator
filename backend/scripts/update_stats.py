from service.game_service import get_teams_from_today_games
from service.player_stats_service import load_last_n_games, get_last_n_stats
from models.team_model import Team
from repositories.player_stats_repository import PlayerStatRepository
from database import SessionLocal
from sqlalchemy.orm import Session
from time import sleep

#update the each player in the team to match their recent stats
def update_team_stats(db: Session, team: Team):
    player_stat_repo = PlayerStatRepository(db)
    for player in team.players:
        n = 5
        player_stat_repo.load_last_n_games(player,n)
        sleep(2)
        print(f"loaded last {n} stats for {player.player_name}")

if __name__ == "__main__":
    update_team_stats()
