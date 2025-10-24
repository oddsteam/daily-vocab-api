from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from app.database import get_db
from app.models import Word, PracticeSession
from app.schemas import SummaryResponse, HistoryItem

router = APIRouter()


@router.get("/summary", response_model=SummaryResponse)
def get_summary(db: Session = Depends(get_db)):
    """Get overall practice statistics"""
    
    # Total practice sessions
    # Average score
    # Total unique words practiced
    
    # Distribution by level
    ...


@router.get("/history", response_model=List[HistoryItem])
def get_history(limit: int = 10, db: Session = Depends(get_db)):
    """Get last 10 practice sessions"""
    ...