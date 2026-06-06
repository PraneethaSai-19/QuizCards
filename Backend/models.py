#import datatypes from sqlalchemy to create table and import base class from database.py
from sqlalchemy import Column , Integer, String
from database import Base

class Flashcard(Base):
    __tablename__ = "flashcards"
    
    #headers
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500))
    answer = Column(String(500))
    category= Column(String(100))