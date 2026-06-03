from pydantic import BaseModel

class ChewResponse(BaseModel):
    total_chews: int
    duration_seconds: float  # <--- Ye line add karein
    message: str