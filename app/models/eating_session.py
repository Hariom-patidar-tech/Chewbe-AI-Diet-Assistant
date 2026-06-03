from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from app.db.database import Base

class EatingSession(Base):
    __tablename__ = "eating_sessions"

    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )

    # user_id aur meal_id yahan se bilkul hata diye gaye hain

    chew_count = Column(
        Integer, 
        default=0
    )
    
    bite_count = Column(
       Integer,
        default = 0  
    )
    
    eating_speed = Column(
        Float, 
        default=0
    )

    started_at = Column(
        DateTime, 
        default=datetime.utcnow
    )

    ended_at = Column(
        DateTime, 
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )