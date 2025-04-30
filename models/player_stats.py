# models/player_game_stat_model.py
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.player_model import Player


class PlayerGameStat(Base):
    __tablename__ = "player_stats"

    id        = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    date      = Column(Date,nullable=False)
    #stats
    pts       = Column(Integer, default=0)
    ast       = Column(Integer, default=0)
    reb       = Column(Integer, default=0)
    stl       = Column(Integer, default=0)
    blk       = Column(Integer, default=0)
    tov       = Column(Integer, default=0)

    player = relationship("Player", back_populates="stats")

