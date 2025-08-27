# DB엔진/세션
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import DB_URL

engine = create_engine(DB_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
