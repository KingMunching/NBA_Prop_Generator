
from database import SessionLocal
from typing import List, Dict, Any, Tuple
from models.player_model import Player
from models.player_stats import PlayerGameStat
from models.team_model import Team
from service.game_service import get_games
from service.team_service import load_team_and_roster
from sqlalchemy import func, desc
from helpers.nba_api_helper import safe_team_roster, get_team_id
import pandas as pd
from nba_api.stats.endpoints import commonplayerinfo, teamplayerdashboard

