
from database import SessionLocal
from typing import List, Dict, Any, Tuple
from models.player_model import Player
from models.player_stats import PlayerGameStat
from models.team_model import Team
from service.game_service import get_teams_from_today_games
from service.team_service import load_team_and_roster
from service.player_stats_service import get_last_n_stats
from sqlalchemy import func, desc
from helpers.nba_api_helper import get_team_id
from nba_api.stats.endpoints import commonplayerinfo, teamplayerdashboard
from repositories.team_repository import TeamRepository
from repositories import prop_repository
from schemas import PropCreate
import json 
from redis_client import get_redis_client
import datetime 
import statistics 



class PropGenerator:
    def __init__(self, prop_type: str, stat: int, threshold: int, num_games:int,
                 num_rec: int, z_score_threshold: float=2.0):
        self.prop_type = prop_type # pts, ast, etc..
        self.stat = stat # ex. 15 pts
        self.threshold = threshold # Minimum Success rate
        self.num_games = num_games # amount of games to analyze
        self.num_rec = num_rec # num of props to return
        self.z_score_threshold = z_score_threshold
        self.db = SessionLocal()

    def __del__(self):
        """Ensure database session is closed when object is destroyed"""
        if hasattr(self, 'db'):
            self.db.close()
    
    def get_player_stat_val(self, recent_stats: List[PlayerGameStat]) -> List[float]:

        stat_map = {
            "PTS": lambda s: s.pts,
            "AST": lambda s: s.ast,
            "REB": lambda s: s.reb,
            "STL": lambda s: s.stl,
            "BLK": lambda s: s.blk,
            "TOV": lambda s: s.tov,
            "3PM": lambda s: s.three_pm
        }
        if self.prop_type not in stat_map:
            return []
        
        values = []
        for s in recent_stats:
            value = stat_map[self.prop_type](s)
            if value is not None:
                values.append(value)
        return values
        
        
    
    """
        Analyze a player's performance against the prop threshold.
        
        Returns:
            Tuple of (success_rate, games_analyzed)
    """
    def analyze_player(self, player: Player) -> Tuple[float, int]:
        
        recent_stats = get_last_n_stats(player, self.num_games)
        if not recent_stats:
            return None

        stat_values = self.get_player_stat_val(recent_stats)
        # Count how many games met the threshold
        games_analyzed = len(stat_values)

        if games_analyzed <= 2:
            return None
        mean_val = statistics.mean(stat_values)
        stdev_val = statistics.stdev(stat_values)

        if stdev_val == 0:
            if self.stat != mean_val:
                return None
            z_score = 0.0
        else:
            z_score = (self.stat - mean_val) / stdev_val

        if abs(z_score) > self.z_score_threshold:
            return None

        overs = sum(1 for v in stat_values if v > self.stat)
        unders = sum(1 for v in stat_values if v < self.stat)
        
        over_rate = overs / games_analyzed
        under_rate = unders/ games_analyzed

        if over_rate > under_rate:
            direction = "Over"
            success_rate = over_rate
        else:
            direction = "Under"
            success_rate = under_rate

        if success_rate < self.threshold:
            return None

        return {
            "success_rate": success_rate,
            "player_avg": round(mean_val, 2),
            "z_score": round(z_score, 2),
            "direction": direction,
            "games_analyzed": games_analyzed,
        }


    
    

    """Generate props for the given players.

        Args:
            players: List of Player objects to generate props for.

        Returns:
            List of dictionaries containing player props with success rates.
    """
    def generate_props(self, players: List[Player]) -> List[Dict[str, Any]]:
        props = []
        for player in players:
           analysis = self.analyze_player(player)
            
           if analysis:
                props.append({
                "nba_id": player.nba_id,
                "player_name": player.player_name,
                "team_nba_id": player.team_nba_id,
                "prop_type": self.prop_type,
                "stat": self.stat,
                **analysis
               }) 
        props.sort(key=lambda x: x["success_rate"], reverse=True)
        return props[:self.num_rec]
    
    def generate_daily_props(self, teams: List[Team]):
        redis_client = get_redis_client()
        
        cache_key = (f"daily_props:{self.prop_type}:{self.stat}:{self.threshold}:{self.num_games}:{self.num_rec}:{self.z_score_threshold}")


        
        try:
            cached_props = redis_client.get(cache_key)
            if cached_props:
                print("cache hit")
                #deserialize JSON string 
                return json.loads(cached_props)
        except Exception as e:
            print(f"something wrong with redis: {e}")

        print("cache missed")
        #if cache missed, proceed with prop logic
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
        props = self.generate_props(unique_players)

        #now store prop in the cahce.

        try:
            redis_client.setex(cache_key, 3600, json.dumps(props))
        except Exception as e:
            print(f"redis error storing prop: {e}")

        return props
    
def create_prop(db, prop: PropCreate, user_id:str):
    return prop_repository.create_prop(db, prop, user_id)

def get_props_by_user(db, user_id):
    return prop_repository.get_props_by_user(db, user_id)

def delete_prop(db, user_id, prop_id):
    prop_repository.delete_prop(db, user_id, prop_id)
