from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db 
from app.services.chew_detection import detect_chews

router = APIRouter()

@router.post("/start")
def start_chew_process(db: Session = Depends(get_db)):
    # Service call
    data = detect_chews(db=db)
    
    # Error checking
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    
    # Sahi response return karo
    return {
        "status": "success",
        "chew_count": data["chew_count"],
        "bite_count": data["bite_count"],
        "active_chewing_seconds": data["active_chew_duration"],
        "message": "Session saved successfully!"
    }