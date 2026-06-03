from pydantic import BaseModel


class AISuggestionResponse(BaseModel):
    suggestion: str