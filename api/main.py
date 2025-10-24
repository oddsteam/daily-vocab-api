from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import WordResponse
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

# CORS middleware for Next.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/word", response_model=WordResponse)
def get_random_word():
    """Get a random word"""
    # TODO Write logic here....
    return [] 


@app.get("/")
def read_root():
    return {
        "message": "Vocabulary Practice API",
        "version": "1.0.0",
        "endpoints": {
            "random_word": "/api/word",
            "validate": "/api/validate-sentence",
            "summary": "/api/summary",
            "history": "/api/history"
        }
    }


@app.get("/health")
def health_check():
    """Check if API is running properly"""
    return {"status": "healthy", "timestamp": datetime.utcnow()}