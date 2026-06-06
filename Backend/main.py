from fastapi import FastAPI
from database import engine
from models import Base
from fastapi.middleware.cors import CORSMiddleware

from routers.flashcards import router as flashcard_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(flashcard_router)