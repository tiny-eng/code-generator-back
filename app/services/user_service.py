from app.models.user_model import User
from app.database import SessionLocal
from app.utils.security import hash_password, verify_password
from fastapi import HTTPException

def create_user(user_data):
    db = SessionLocal()

    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)

    db_user = User(
        nickname=user_data.nickname,
        email=user_data.email,
        password=hashed_pw,
        role=user_data.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user


def authenticate_user(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    return user

