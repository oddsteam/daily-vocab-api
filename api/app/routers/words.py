from fastapi import APIRouter, Depends, HTTPException
import random

from app.models import Word
from app.schemas import WordResponse

router = APIRouter()


words = [
    { "word": "Ephemeral", "meaning": "Lasting for a very short time.", "difficulty": "Advanced" },
    { "word": "Ubiquitous", "meaning": "Present, appearing, or found everywhere.", "difficulty": "Intermediate" },
    { "word": "Mellifluous", "meaning": "(Of a voice or words) sweet or musical; pleasant to hear.", "difficulty": "Advanced" },
    { "word": "Serendipity", "meaning": "The occurrence and development of events by chance in a happy or beneficial way.", "difficulty": "Intermediate" },
    { "word": "Happy", "meaning": "Feeling or showing pleasure or contentment.", "difficulty": "Beginner" },
    { "word": "Run", "meaning": "Move at a speed faster than a walk, never having both or all the feet on the ground at the same time.", "difficulty": "Beginner" }
]

@router.get("/word", response_model=WordResponse)
def get_random_word():
    ... 