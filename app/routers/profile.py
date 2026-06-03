from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.profile import Profile
from app.models.user import User
from app.schemas.profile import ProfileCreate
from app.core.security import get_current_user

# Yahan se prefix aur tags hata diya
router = APIRouter()

@router.post("/create")
def create_or_update_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 1. Check karein ki kya user ki pehle se koi profile exist karti hai
    existing_profile = db.query(Profile).filter(
        Profile.user_id == current_user.id
    ).first()

    # 2. AGAR PROFILE EXIST KARTI HAI -> UPDATE KAREIN
    if existing_profile:
        existing_profile.age = profile.age
        existing_profile.gender = profile.gender
        existing_profile.height = profile.height
        existing_profile.weight = profile.weight
        existing_profile.target_weight = profile.target_weight
        existing_profile.body_type = profile.body_type
        existing_profile.diet_preference = profile.diet_preference
        existing_profile.fitness_goal = profile.fitness_goal
        existing_profile.activity_level = profile.activity_level
        
        db.commit()
        db.refresh(existing_profile)
        return {"message": "Profile updated successfully"}

    # 3. AGAR PROFILE NAHI HAI -> NEW CREATE KAREIN
    new_profile = Profile(
        user_id=current_user.id,
        age=profile.age,
        gender=profile.gender,
        height=profile.height,
        weight=profile.weight,
        target_weight=profile.target_weight,
        body_type=profile.body_type,
        diet_preference=profile.diet_preference,
        fitness_goal=profile.fitness_goal,
        activity_level=profile.activity_level
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return {"message": "Profile created successfully"}