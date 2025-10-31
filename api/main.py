from fastapi import FastAPI
from app.schemas import WordResponse

# Initialize FastAPI app
app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

@app.get("/api/word", response_model=WordResponse)
def get_random_word():
    """Get a random word"""
    # TODO Write logic here....
    return WordResponse(
        id=2,
        word='book',
        definition='Reading material',
        difficulty_level='Beginner'
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