# 비밀번호 해시/JWT 발급
from datetime import datetime
from jose import jwt
from passlib.context import CryptContext
from .config import JWT_SECRET, JWT_ALG, access_delta

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(raw: str) -> str:
    return pwd_ctx.hash(raw)

def verify_password(raw: str, hashed: str) -> bool:
    return pwd_ctx.verify(raw, hashed)

def create_access_token(sub: int) -> str:
    exp = datetime.utcnow() + access_delta()
    return jwt.encode({"sub": str(sub), "exp": exp}, JWT_SECRET, algorithm=JWT_ALG)