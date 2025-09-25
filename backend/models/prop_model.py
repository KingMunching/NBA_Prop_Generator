import uuid
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base

class Prop(Base):
    __tablename__ = "props"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  
    user_id = Column(UUID(as_uuid=True), nullable=False)
    prop_type = Column(String, nullable=False)
    stat = Column(Integer, nullable=False)
    threshold = Column(Float, nullable=False)
    num_games = Column(Integer, nullable=False)
    player_name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
