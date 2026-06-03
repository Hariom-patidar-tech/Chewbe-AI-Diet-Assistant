from pydantic import BaseModel


class ProfileCreate(BaseModel):
    age: int
    gender: str
    height: int
    weight: int
    target_weight: int
    body_type: str
    diet_preference: str
    fitness_goal: str
    activity_level: str