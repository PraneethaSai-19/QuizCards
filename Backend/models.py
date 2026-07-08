#import datatypes from sqlalchemy to create table and import base class from database.py
from sqlalchemy import Column , Integer, String , ForeignKey , DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base

class Flashcard(Base):
    __tablename__ = "flashcards"
    
    #headers
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500))
    answer = Column(String(500))
    category= Column(String(100))
    user_id = Column(Integer , ForeignKey("users.id"))
    owner = relationship(
        "User" , back_populates="flashcards"
    )
    
class User(Base):
    __tablename__ = "users"
    id = Column(
        Integer,
        primary_key = True,
        index=True
    )
    username = Column(
        String(100),
        unique = True
    )
    email = Column(
        String(100),
        unique = True
    )
    password = Column(
        String(255)
    )
    flashcards = relationship(
        "Flashcard", back_populates="owner"
    )
    quiz_scores = relationship(
        "QuizScore",
        back_populates="user"
    )

class QuizScore(Base):
    __tablename__ = "quiz_scores"
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    
    
    score = Column(Integer)
    total_questions = Column(Integer)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )
    user = relationship(
        "User",
        back_populates="quiz_scores"
    )