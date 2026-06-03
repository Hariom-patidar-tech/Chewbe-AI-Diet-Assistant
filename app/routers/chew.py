from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db 
from app.services.chew_detection import detect_chews

router = APIRouter()

@router.post("/start")
def start_chew_process(db: Session = Depends(get_db)):
    # Ab service ko sirf database session chahiye
    data = detect_chews(db=db)
    
    if "error" in data:
        raise HTTPException(status_code=500, detail=data["error"])
    
    return {
        "status": "success",
        "total_chews": data["total_chews"],
        "active_chewing_seconds": data.get("active_chew_duration", 0),
        "message": "Session saved successfully !"
    }