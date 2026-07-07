from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate, UserLogin

from security import create_access_token
from passlib.context import CryptContext

from jose import jwt 
from datetime import datetime , timedelta

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



# Signup
@router.post("/signup")
def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    hashed_password = pwd_context.hash(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User created successfully"
    }


# Login
@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    valid_password =  pwd_context.verify(
            user.password,
            existing_user.password
        )

    if not valid_password:
        raise HTTPException(
            status_code=401,
            detail="Incorrect password"
        )

    access_token = create_access_token(
        data = {
            "sub" : existing_user.email
        }
    )
    
    return{
        "access_token" : access_token,
        "token_type" : "bearer"
    }