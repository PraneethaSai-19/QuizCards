from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import QuizScore , User
from schemas import QuizScoreCreate
from security import get_current_user

router = APIRouter()

@router.post("/quiz-score")
def save_quiz_score(
    quiz: QuizScoreCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_score = QuizScore(
        score = quiz.score,
        total_questions = quiz.total_questions,
        user_id = current_user.id
    )
    db.add(new_score)
    db.commit()
    db.refresh(new_score)
    
    return{
        "message": "Quiz score saved succesfully!"
    }
    