from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date


class PlayerBase(BaseModel):
    name: str
    nba_id: int
    team_id: int


class PlayerCreate(PlayerBase):
    pass


class PlayerResponse(PlayerBase):
    id: int

    class Config:
        from_attributes = True


class TeamBase(BaseModel):
    name: str
    nba_id: int


class TeamCreate(TeamBase):
    pass


class TeamResponse(TeamBase):
    id: int
    players: Optional[List[PlayerResponse]] = []

    class Config:
        from_attributes = True


class PlayerGameStatBase(BaseModel):
    player_id: int
    date: date
    min: Optional[str] = "0"
    pts: Optional[int] = 0
    ast: Optional[int] = 0
    reb: Optional[int] = 0
    stl: Optional[int] = 0
    blk: Optional[int] = 0
    tov: Optional[int] = 0


class PlayerGameStatCreate(PlayerGameStatBase):
    pass


class PlayerGameStatResponse(PlayerGameStatBase):
    id: int

    class Config:
        from_attributes = True


class PlayerWithStats(PlayerResponse):
    stats: List[PlayerGameStatResponse] = []

    class Config:
        from_attributes = True


"""
class PropResponse(BaseModel):
    player_id: int
    player_name: str
    success_rate: float
    games_analyzed: int
    prop_type: str
    stat: int
"""

class PropResponse(BaseModel):
    prop_type: str
    stat: int
    threshold: float
    num_games: int
    num_rec: int

class PropCreate(BaseModel):
    user_id: str
    player_name: str
    prop_type: str
    prop_value: float
    threshold: str
    game_date: date
