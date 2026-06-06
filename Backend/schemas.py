from pydantic import BaseModel

class FlashcardCreate(BaseModel):
    question : str
    answer: str
    category: str
class FlashcardUpdate(BaseModel):
    question : str
    answer: str
    category: str