from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user_model import User
from app.crud.user_crud import get_by_email, get_by_id, create_user
from app.utils.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/token")

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

    db_user = create_user(db, user)

    token = create_access_token({"id": db_user.id, "email": db_user.email})

    return {
        "id": user.id,
        "email": user.email,
        "nickname": user.nickname,
        "role": user.role,
        "access_token": token
    }

def authenticate_user(login_data: UserLogin, db: Session):
    user = get_by_email(db, login_data.email)
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(400, "Invalid credentials")
    
    token = create_access_token({"id": user.id, "email": user.email})

    return {
        "id": user.id,
        "email": user.email,
        "nickname": user.nickname,
        "role": user.role,
        "access_token": token
    }


