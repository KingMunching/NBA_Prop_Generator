from database import SessionLocal
from typing import List, Dict, Any, Tuple
from models.player_model import Player
from models.player_stats import PlayerGameStat
from models.team_model import Team
from service.game_service import get_teams_from_today_games
from service.team_service import load_team_and_roster
from service.player_stats_service import get_last_n_stats
from sqlalchemy import func, desc
from helpers.nba_api_helper import safe_team_roster, get_team_id
from nba_api.stats.endpoints import commonplayerinfo, teamplayerdashboard
from repositories.team_repository import TeamRepository
from random import shuffle


class PropGenerator:
    def __init__(self, prop_type: str, stat: int, threshold: int, num_games: int,
                 num_rec: int):
        self.prop_type = prop_type # pts, ast, etc..
        self.stat = stat # ex. 15 pts
        self.threshold = threshold # Minimum Success rate
        self.num_games = num_games # amount of games to analyze
        self.num_rec = num_rec # num of props to return
        self.db = SessionLocal()

    def __del__(self):
        """Ensure database session is closed when object is destroyed"""
        if hasattr(self, 'db'):
            self.db.close()
    
    """
        Analyze a player's performance against the prop threshold for both over and under.
        
        Returns:
            Tuple of (over_success_rate, under_success_rate, games_analyzed)
    """
    def analyze_player(self, player: Player) -> Tuple[float, float, int]:
        
        recent_stats = get_last_n_stats(player, self.num_games)
        if not recent_stats:
            return 0.0, 0.0, 0
        
        games_analyzed = len(recent_stats)
        if games_analyzed == 0:
            return 0.0, 0.0, 0

        over_successes = self.count_successes(recent_stats, "over")
        under_successes = self.count_successes(recent_stats, "under")
        
        over_success_rate = over_successes / games_analyzed
        under_success_rate = under_successes / games_analyzed
        
        return over_success_rate, under_success_rate, games_analyzed
    
    """Count how many games met the threshold for the given prop type and bet type.

    Args:
        recent_stats: List of recent PlayerGameStat objects.
        bet_type: "over" or "under"

    Returns:
        Number of games that met the criteria based on bet_type.
    """
    def count_successes(self, recent_stats: List[PlayerGameStat], bet_type: str) -> int:
        count = 0
        for stat in recent_stats:
            stat_value = self.get_stat_value(stat)
            
            if bet_type == "over":
                if stat_value >= self.stat:
                    count += 1
            elif bet_type == "under":
                if stat_value < self.stat:
                    count += 1
        return count
    
    """Get the stat value based on prop_type.

    Args:
        stat: PlayerGameStat object.

    Returns:
        The numeric value for the specified prop_type.
    """
    def get_stat_value(self, stat: PlayerGameStat) -> int:
        if self.prop_type == "pts":
            return stat.pts
        elif self.prop_type == "ast":
            return stat.ast
        elif self.prop_type == "reb":
            return stat.reb
        elif self.prop_type == "stl":
            return stat.stl
        elif self.prop_type == "blk":
            return stat.blk
        elif self.prop_type == "tov":
            return stat.tov
        elif self.prop_type == "pts+reb+ast":
            return stat.pts + stat.reb + stat.ast
        else:
            return 0
    

    """Generate props for the given players, calculating both over and under bets.

        Args:
            players: List of Player objects to generate props for.

        Returns:
            List of dictionaries containing player props with success rates for both over and under bets.
    """
    def generate_props(self, players: List[Player]) -> List[Dict[str, Any]]:
        props = []
        for player in players:
            over_success_rate, under_success_rate, games_analyzed = self.analyze_player(player)
            
            if games_analyzed > 0:
                # Add over bet if it meets threshold
                if over_success_rate >= self.threshold:
                    props.append({
                        "player_id": player.id,
                        "player_name": player.name,
                        "success_rate": over_success_rate,
                        "games_analyzed": games_analyzed,
                        "prop_type": self.prop_type,
                        "stat": self.stat,
                        "bet_type": "over"
                    })
                
                # Add under bet if it meets threshold
                if under_success_rate >= self.threshold:
                    props.append({
                        "player_id": player.id,
                        "player_name": player.name,
                        "success_rate": under_success_rate,
                        "games_analyzed": games_analyzed,
                        "prop_type": self.prop_type,
                        "stat": self.stat,
                        "bet_type": "under"
                    })
        
        # Sort by success rate (highest first) and return top num_rec
        props.sort(key=lambda x: x["success_rate"], reverse=True)
        return props[:self.num_rec]
    
    def generate_daily_props(self, teams: List[Team]):
        db = SessionLocal()
        try:
            team_repo = TeamRepository(db)
            if not teams:
                print("No teams found for today's games.")
                return []

            all_players = []
            for team in teams:
                for player in team_repo.get_key_players(team):
                    all_players.append(player)
            shuffle(all_players)
            # Remove duplicates if any (players playing in multiple games)
            unique_players = list({player.id: player for player in all_players}.values())

            # Generate props for the collected players
            return self.generate_props(unique_players)

        except Exception as e:
            print(f"An error occurred: {e}")
            raise

        finally:
            db.close()
