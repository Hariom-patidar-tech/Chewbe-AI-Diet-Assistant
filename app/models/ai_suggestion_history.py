from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text # Text import karein
from sqlalchemy.sql import func
from app.db.database import Base

class AISuggestionHistory(Base):
    __tablename__ = "ai_suggestion_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))
    # String(1000) ki jagah Text() ka use karein
    suggestion = Column(Text) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())