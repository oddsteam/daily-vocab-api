from pydantic import BaseModel
from datetime import datetime
from typing import List


class WordResponse(BaseModel):
    id: int
    word: str
    definition: str
    difficulty_level: str
    
    class Config:
        from_attributes = True


class ValidateSentenceRequest(BaseModel):
    word_id: int
    sentence: str


class ValidateSentenceResponse(BaseModel):
    score: float
    level: str
    suggestion: str
    corrected_sentence: str


class SummaryResponse(BaseModel):
    total_practices: int
    average_score: float
    total_words_practiced: int
    level_distribution: dict


class HistoryItem(BaseModel):
    id: int
    word: str
    user_sentence: str
    score: float
    feedback: str
    practiced_at: datetime

    class Config:
        from_attributes = True