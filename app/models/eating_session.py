from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from app.db.database import Base
from datetime import datetime

class EatingSession(Base):
    __tablename__ = "eating_sessions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) # Zaroori
    meal_id = Column(Integer, ForeignKey("meals.id"), nullable=True)
    chew_count = Column(Integer, default=0)
    bite_count = Column(Integer, default=0)
    eating_speed = Column(Float, default=0)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)