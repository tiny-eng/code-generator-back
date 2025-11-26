from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from .database import SessionLocal
from app.crud.user_crud import get_by_email
from app.utils.security import decode_access_toke
from app.models.user_model import User


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
