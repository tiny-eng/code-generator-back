from passlib.context import CryptContext


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