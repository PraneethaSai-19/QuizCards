#import datatypes from sqlalchemy to create table and import base class from database.py
from sqlalchemy import Column , Integer, String , ForeignKey
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