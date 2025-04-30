from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Team(Base):
    __tablename__ = "teams"
    name = Column(String, unique=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    nba_id = Column(Integer, unique=True, nullable=False, index=True)
    players = relationship("Player", back_populates="team")