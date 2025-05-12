
from database import SessionLocal
from typing import List, Dict, Any, Tuple
from models.player_model import Player
from models.player_stats import PlayerGameStat
from models.team_model import Team
from service.game_service import get_teams_from_today_games
from service.team_service import load_team_and_roster
from sqlalchemy import func, desc
from helpers.nba_api_helper import safe_team_roster, get_team_id
from nba_api.stats.endpoints import commonplayerinfo, teamplayerdashboard
from repositories.team_repository import TeamRepository

class PropGenerator:
    def __init__(self, prop_type: str, stat: int, threshold: int, num_games:int,
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
        Analyze a player's performance against the prop threshold.
        
        Returns:
            Tuple of (success_rate, games_analyzed)
    """
    def analyze_player(self, player: Player) -> Tuple[float, int]:
        recent_stats = (
            self.db.query(PlayerGameStat)
            .filter(PlayerGameStat.player_id == player.id)
            .order_by(desc(PlayerGameStat.date))
            .limit(self.num_games)
            .all()
        )
        if not recent_stats:
            return 0.0, 0
        # Count how many games met the threshold
        games_analyzed = len(recent_stats)
        if games_analyzed == 0:
            return 0.0, 0

        sucesses = self.count_sucesses(recent_stats)
        sucesses_rate = sucesses / games_analyzed
        return sucesses_rate, games_analyzed
    
    """Count how many games met the threshold for the given prop type.

    Args:
        recent_stats: List of recent PlayerGameStat objects.

    Returns:
        Number of games that met/exceeded the threshold.
    """
    def count_sucesses(self, recent_stats: List[PlayerGameStat]) -> int:
        count = 0
        for stat in recent_stats:
            if self.prop_type == "pts" and stat.pts >= self.stat:
                count += 1
            elif self.prop_type == "ast" and stat.ast >= self.stat:
                count += 1
            elif self.prop_type == "reb" and stat.reb >= self.stat:
                count += 1
            elif self.prop_type == "stl" and stat.stl >= self.stat:
                count += 1
            elif self.prop_type == "blk" and stat.blk >= self.stat:
                count += 1
            elif self.prop_type == "tov" and stat.tov >= self.stat:
                count += 1
            elif self.prop_type == "pts+reb+ast" and (stat.pts + stat.reb + stat.ast) >= self.stat:
                count += 1
        return count
    

    """Generate props for the given players.

        Args:
            players: List of Player objects to generate props for.

        Returns:
            List of dictionaries containing player props with success rates.
    """
    def generate_props(self, players: List[Player]) -> List[Dict[str, Any]]:
        props = []
        for player in players:
            success_rate, games_analyzed = self.analyze_player(player)
            if games_analyzed > 0 and success_rate >= self.threshold:
               props.append({
                   "player_id": player.id,
                   "player_name": player.name,
                   "success_rate": success_rate,
                   "games_analyzed": games_analyzed,
                   "prop_type": self.prop_type,
                   "stat": self.stat
               }) 
        props.sort(key=lambda x: x["success_rate"], reverse=True)
        return props[:self.num_rec]
    
    def generate_daily_props(self, teams: List[Team]):
        
        if not teams:
            print("No teams found for today's games.")
            return []

        all_players = []
        for team in teams:
            for player in team.players:
                all_players.append(player)

        # Remove duplicates if any (players playing in multiple games)
        unique_players = list({player.id: player for player in all_players}.values())

        # Generate props for the collected players
        return self.generate_props(unique_players)