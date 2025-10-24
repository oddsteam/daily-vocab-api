from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Word, PracticeSession
from app.schemas import ValidateSentenceRequest, ValidateSentenceResponse
from app.utils import mock_ai_validation

router = APIRouter()


@router.post("/validate-sentence", response_model=ValidateSentenceResponse)
def validate_sentence(
    request: ValidateSentenceRequest,
    db: Session = Depends(get_db)
):
    """
    Receive user sentence and validate it (mock AI)
    Save results to database
    """
    # Get word data
    # Mock AI validation
    # Save to database
    ...