from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    nickname: str
    email: str
    password: str
    role: str = "client"

class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    nickname: str
    email: str
    role: str
    access_token: str

    model_config = ConfigDict(from_attributes=True)

