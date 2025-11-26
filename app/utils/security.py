from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Hash a password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your_super_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

MAX_BCRYPT_LENGTH = 72

def hash_password(password: str) -> str:
    truncated = password[:MAX_BCRYPT_LENGTH]
    return pwd_context.hash(truncated)

# Verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    truncated = plain_password[:MAX_BCRYPT_LENGTH]
    return pwd_context.verify(truncated, hashed_password)

def create_access_toke(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_toke(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None