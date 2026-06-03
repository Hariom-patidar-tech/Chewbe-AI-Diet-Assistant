from pydantic import BaseModel


class MealCreate(BaseModel):
    meal_name: str
    category: str
    calories: int
    protein: int
    image_url: str | None = None