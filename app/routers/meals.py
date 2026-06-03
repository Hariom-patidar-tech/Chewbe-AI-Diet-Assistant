from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.meal import Meal
from app.models.user import User # Import ensure karein
from app.models.profile import Profile
from app.models.ai_suggestion_history import AISuggestionHistory
from app.schemas.meal import MealCreate
from app.core.security import get_current_user
from app.services.ai_service import generate_meal_suggestion

router = APIRouter(prefix="/meals", tags=["Meals"])

@router.post("/add")
def add_meal_and_get_ai(
    meal: MealCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) # Yahan User type hint add kiya
):
    new_meal = Meal(
        user_id=current_user.id,
        meal_name=meal.meal_name,
        category=meal.category,
        calories=meal.calories,
        protein=meal.protein
    )
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)

    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    all_meals = db.query(Meal).filter(Meal.user_id == current_user.id).all()

    ai_suggestion = generate_meal_suggestion(profile, all_meals)

    new_history = AISuggestionHistory(
        user_id=current_user.id,
        meal_id=new_meal.id,
        suggestion=ai_suggestion
    )
    db.add(new_history)
    db.commit()

    return {
        "message": "Meal added successfully",
        "ai_suggestion": ai_suggestion
    }

@router.get("/history")
def get_user_history(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) # Yahan User type hint add kiya
):
    # Join query ka sahi istemal
    results = db.query(Meal, AISuggestionHistory).join(
        AISuggestionHistory, Meal.id == AISuggestionHistory.meal_id
    ).filter(Meal.user_id == current_user.id).all()
    
    # Data ko format karke return karna
    history_list = []
    for meal, suggestion in results:
        history_list.append({
            "meal_name": meal.meal_name,
            "calories": meal.calories,
            "protein": meal.protein,
            "suggestion": suggestion.suggestion,
            "date": suggestion.created_at # History table mein time hota hai
        })
    
    return history_list