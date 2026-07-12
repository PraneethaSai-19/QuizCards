from pydantic import BaseModel

class FlashcardCreate(BaseModel):
    question : str
    answer: str
    category: str
class FlashcardUpdate(BaseModel):
    question : str
    answer: str
    category: str
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
class UserLogin(BaseModel):
    email: str
    password: str

class QuizScoreCreate(BaseModel):
    score : int
    total_questions: int