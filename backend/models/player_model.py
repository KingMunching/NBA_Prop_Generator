from sqlalchemy import Column, Integer, String, ForeignKey, Double
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    nba_id = Column(Integer, unique=True, nullable=False, index=True)
    player_name = Column(String)
    team_nba_id = Column(Integer, ForeignKey("teams.nba_id"), nullable=False)

    
    team = relationship(
        "Team",
        back_populates="players",
        primaryjoin="Player.team_nba_id==Team.nba_id"
    )

    stats = relationship(
        "PlayerGameStat",
        back_populates="player",
        primaryjoin="Player.nba_id==PlayerGameStat.player_nba_id",  
        order_by="desc(PlayerGameStat.date)",
        lazy="dynamic"
    )

    
