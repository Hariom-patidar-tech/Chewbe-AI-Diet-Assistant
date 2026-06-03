from pydantic import BaseModel

class ChewResult(BaseModel):
    chew_count: int
    feedback: str