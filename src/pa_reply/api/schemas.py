from pydantic import BaseModel, Field
from typing import Literal, Optional

Tone = Literal["mild", "medium", "nuclear"]
Length = Literal["short", "medium", "long"]

class GenerateRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    context: Optional[str] = Field(None, max_length=4000)
    tone: Tone = "medium"
    length: Length = "short"
    language: str = Field("en", min_length=2, max_length=8)

class GenerateResponse(BaseModel):
    reply: str
    model_id: str