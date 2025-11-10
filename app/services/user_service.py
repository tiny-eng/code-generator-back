from app.models.user_model import User
from app.database import SessionLocal

def create_user(user_data):
    db = SessionLocal()
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
