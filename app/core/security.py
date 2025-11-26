from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "123456"   # change this
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
