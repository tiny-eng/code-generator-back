from pydantic import BaseModel

class UserCreate(BaseModel):
    nickname: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    nickname: str
    email: str

    class Config:
        orm_mode = True

        