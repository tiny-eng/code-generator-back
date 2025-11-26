from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user_model import User
from app.crud.user_crud import get_by_email, get_by_id, create_user
from app.utils.security import hash_password, verify_password

def create_user_service(user_data: UserCreate, db: Session):
    existing_user = get_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user_data.password)

    user = User(
        nickname=user_data.nickname,
        email=user_data.email,
        password=hashed_pw,
        role=user_data.role
    )

    return create_user(db, user)

def autheticate_user_service(login_data: UserLogin, db: Session):
    email = login_data.email
    password = login_data.password

    user = get_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    return user
