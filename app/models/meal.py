from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from app.db.database import Base


class Meal(Base):
    __tablename__ = "meals"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    meal_name = Column(
    String(100),
    nullable=False,
    index=True
)

    category = Column(
        String(50),
        nullable=False
    )
    # breakfast, lunch, dinner, snack

    calories = Column(Integer)

    protein = Column(Integer)

    image_url = Column(String(500))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )