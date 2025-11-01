from fastapi import FastAPI
from app.schemas import WordResponse
from fastapi import HTTPException
from app.routers import words

# Initialize FastAPI app
app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

app.include_router(words.router, prefix="/api", tags=["words"])

@app.get("/api/word" , response_model = WordResponse)
def get_random_word():
    """Get a random word"""
    # TODO Write logic here....
    word = []
    if len(word) == 0:
        raise HTTPException(
            status_code = 404,
            detail = "No words available in database"
        )

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