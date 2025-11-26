from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.security import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# Hash a password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


MAX_BCRYPT_LENGTH = 72

def hash_password(password: str) -> str:
    truncated = password[:MAX_BCRYPT_LENGTH]
    return pwd_context.hash(truncated)

# Verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password[:MAX_BCRYPT_LENGTH]
    return pwd_context.verify(truncated, hashed_password)


def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)