from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import create_user_service, authenticate_user
from app.dependencies import get_db, get_current_admin, get_current_user
from app.utils.security import create_access_token


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)

@router.post("/signin", response_model=UserResponse)
def signin(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(user, db)



@router.get("/profile")
def get_profile(current_user = Depends(get_current_user)):
    return current_user




