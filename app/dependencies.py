from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from .database import SessionLocal
from app.crud.user_crud import get_by_id
from app.utils.security import SECRET_KEY, ALGORITHM
from app.models.user_model import User
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/signin")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("id")

        if user_id is None:
            raise credential_exception
        

    except JWTError:
        raise credential_exception
    
    user = get_by_id(db, user_id)

    if user is None:
        raise credential_exception
    
    return user

def get_current_admin(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )
    return current_user
