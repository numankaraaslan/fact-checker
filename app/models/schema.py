from pydantic import BaseModel
from typing import List

class FactCheckRequest(BaseModel):
    query: str

class Citation(BaseModel):
    title: str
    url: str
    content: str

class FactCheckResponse(BaseModel):
    verdict: str
    reasoning: str
    citations: List[Citation]

