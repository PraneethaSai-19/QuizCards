from fastapi import APIRouter, HTTPException , Depends
from database import SessionLocal , get_db
from models import Flashcard
from schemas import FlashcardCreate, FlashcardUpdate
from sqlalchemy.orm import Session

from security import get_current_user
from models import User

router = APIRouter()

# Create Flashcard
@router.post("/flashcards")
def create_flashcard(card: FlashcardCreate , db: Session = Depends(get_db) , current_user: User = Depends(get_current_user)):

    # db = SessionLocal()

    new_card = Flashcard(
        question=card.question,
        answer=card.answer,
        category=card.category,
        user_id = current_user.id
    )

    db.add(new_card)
    db.commit()
    db.refresh(new_card)

    return {
        "message": "Flashcard created successfully",
        "data": new_card
    }

# Get All Flashcards
@router.get("/flashcards")
def get_flashcards(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):

    # db = SessionLocal()

    cards = db.query(Flashcard).filter(Flashcard.user_id == current_user.id).all()

    return cards

# Delete Flashcard
@router.delete("/flashcards/{card_id}")
def delete_flashcard(card_id: int, db: Session = Depends(get_db) , current_user: User = Depends(get_current_user)):

    # db = SessionLocal()

    card = db.query(Flashcard).filter(
        Flashcard.id == card_id,
        Flashcard.user_id == current_user.id
    ).first()

    if not card:
        raise HTTPException(
            status_code=404,
            detail="Flashcard not found"
        )

    db.delete(card)
    db.commit()

    return {
        "message": "Flashcard deleted successfully"
    }

# Update Flashcard
@router.put("/flashcards/{card_id}")
def update_flashcard(
    card_id: int,
    update_card: FlashcardUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # db = SessionLocal()

    card = db.query(Flashcard).filter(
        Flashcard.id == card_id,
        Flashcard.user_id == current_user.id
    ).first()

    if not card:
        raise HTTPException(
            status_code=404,
            detail="Flashcard not found"
        )

    card.question = update_card.question
    card.answer = update_card.answer
    card.category = update_card.category

    db.commit()
    db.refresh(card)

    return {
        "message": "Flashcard updated successfully",
        "data": card
    }