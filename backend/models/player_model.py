from sqlalchemy import Column, Integer, String, ForeignKey, Double
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__ = "players"
    name = Column(String)
    id = Column(Integer, primary_key=True, index=True)
    nba_id = Column(Integer, unique=True, nullable=False, index=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team  = relationship("Team", back_populates="players")

    stats = relationship(
        "PlayerGameStat",
        back_populates="player",
        order_by="desc(PlayerGameStat.date)",
        lazy="dynamic"
    )