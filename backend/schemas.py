from pydantic import BaseModel, Field, computed_field
from typing import List, Optional
from datetime import date, datetime

from uuid import UUID


class PlayerBase(BaseModel):
    player_name: str
    nba_id: int
    team_nba_id: int

    class Config:
        from_attributes = True


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
    nba_id: int
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


class PropRequestBase(BaseModel):
    prop_type: str = Field(..., description="Type of prop (pts, ast, reb, etc.)")
    stat: int = Field(..., description="Threshold value (e.g., 15 points)")
    num_games: int = Field(20, description="Number of games to analyze")
    num_rec: int = Field(5, description="Number of recommendations to return")
    threshold: float = Field(0.8, descriptivon="Minimum success rate (0.0-1.0)")
    z_score_threshold: float = Field(0.5, description="Max Z-Score distance from the mean") 

class PropGeneratedResponse(PlayerBase):
    success_rate: float
    games_analyzed: int
    prop_type: str
    stat: int
    player_avg: float
    z_score: float
    direction: str
   

class PropResponse(BaseModel):
    id: UUID
    user_id: UUID
    prop_type: str
    stat: int
    threshold: float
    num_games: int
    player_name: str
    nba_id: int
    created_at: datetime 
    success_rate: float

    @computed_field
    @property
    def headshot_url(self) -> str:
        return f"https://cdn.nba.com/headshots/nba/latest/260x190/{self.nba_id}.png"
    

"""
    returning a list of saved bets to the user
"""

class PropCreate(BaseModel):
    prop_type: str
    stat: int
    threshold: float
    num_games: int
    player_name: str
    nba_id: int
    success_rate: float

class PropSavedResponse(PropCreate):
    id: UUID
    created_at: datetime

class UserPropsResponse(BaseModel):
    props: List[PropResponse]

    
