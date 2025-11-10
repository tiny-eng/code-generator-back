from fastapi import APIRouter, Depends, Query
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user

from pydantic import BaseModel

router = APIRouter()

# @router.post("/signup/", response_model=UserResponse)
# async def read_root():
#     return {"Hello": "World"}

@router.post("/signup", response_model=UserResponse)
async def create_new_user(user: UserCreate):
    return await create_user(user)

# Define a request model
# class UserCreate(BaseModel):
#     nickname: str
#     email: str
#     password: str

# # POST route
# @router.post("/signup")
# async def create_user(user: UserCreate):
#     # In a real app, you’d save to the database here
#     return {"message": "User created successfully", "user": user}


