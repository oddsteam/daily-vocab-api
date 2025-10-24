from pydantic import BaseModel

class WordResponse(BaseModel):
    id: int
    word: str
    definition: str
    difficulty_level: str
    
    class Config:
        from_attributes = True