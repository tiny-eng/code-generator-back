from fastapi import APIRouter, Depends, Query
from app.schemas.user_schema import UserCreate, UserResponse, UserLogin
from app.services.user_service import create_user, authenticate_user

from pydantic import BaseModel

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def create_new_user(user: UserCreate):
    return create_user(user)

@router.post("/signin", response_model=UserResponse)
async def signin(user: UserLogin):
    authenticated_user = authenticate_user(user.email, user.password)
    return authenticated_user



