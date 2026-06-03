from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.db.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
    Integer,
    ForeignKey("users.id"),
    nullable=False,
    unique=True
)

    age = Column(Integer)

    gender = Column(String(20))

    height = Column(Integer)

    weight = Column(Integer)

    target_weight = Column(Integer)

    body_type = Column(String(50))

    diet_preference = Column(String(50))

    fitness_goal = Column(String(100))

    activity_level = Column(String(50))