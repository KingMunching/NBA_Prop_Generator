from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class PlayerGameStat(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True, index=True)
    player_nba_id = Column(Integer, ForeignKey("players.nba_id"), nullable=False)
    date = Column(Date, nullable=False)

    # stats
    min = Column(String, default='0')
    pts = Column(Integer, default=0)
    ast = Column(Integer, default=0)
    reb = Column(Integer, default=0)
    stl = Column(Integer, default=0)
    blk = Column(Integer, default=0)
    tov = Column(Integer, default=0)

    player = relationship(
        "Player",
        back_populates="stats",
        primaryjoin="Player.nba_id==PlayerGameStat.player_nba_id"
    )
