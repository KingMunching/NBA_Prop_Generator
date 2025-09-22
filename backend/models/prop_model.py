from sqlalchemy import Column, String, Integer, Float, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import uuid

class Prop(Base):
    __tablename__ = "props"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("auth.users.id", ondelete="CASCADE"), nullable=False)
    prop_type = Column(String, nullable=False)
    stat = Column(Integer, nullable=False)
    threshold = Column(Float, nullable=False)
    num_games = Column(Integer, nullable=False)
    num_players = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default="now()")
