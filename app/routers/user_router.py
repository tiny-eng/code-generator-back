from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.user_service import create_user_service, autheticate_user_service
from app.dependencies import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)

@router.post("/signin", response_model=UserResponse)
def signin(user: UserLogin, db: Session = Depends(get_db)):
    authenticate_user = autheticate_user_service(user, db)
    return authenticate_user

