from fastapi import FastAPI
from app.db.database import Base, engine

# Models import
from app.models.user import User
from app.models.otp import OTPVerification
from app.models.profile import Profile
from app.models.meal import Meal
from app.models.eating_session import EatingSession


# Routers import
from app.routers.meals import router as meals_router

from app.routers.profile import router as profile_router
from app.routers.chew import router as chew_router
from app.routers.auth import router as auth_router

# Database tables create karein
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Chewbe API",
    description="AI Based Chew Detection and Meal Tracking API",
    version="1.0.0"
)
from fastapi.middleware.cors import CORSMiddleware
from app.main import app # Ya jahan aapne app initialize kiya hai

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Sabhi sources ko allow kar rahe hain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Routers ko include karein
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# Prefix hata dein kyunki router file mein pehle se hai
app.include_router(profile_router, prefix="/profile", tags=["User Profile"])
app.include_router(meals_router, prefix="/meals", tags=["Meals"])

app.include_router(chew_router, prefix="/chew", tags=["Chew Detection"])

@app.get("/", tags=["Root"])
def home():
    return {
        "message": "Chewbe API is running successfully!",
        "status": "healthy"
    } # Yahan bracket sahi kar diya hai