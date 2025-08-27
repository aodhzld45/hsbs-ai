# Pydantic 스키마
from pydantic import BaseModel, EmailStr, Field
from typing import List

class HealthOut(BaseModel):
    ok: bool = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class StockCreate(BaseModel):
    symbol: str
    name: str

class StockUpdate(BaseModel):
    name: str

class StockOut(BaseModel):
    id: int
    symbol: str
    name: str
    class Config: from_attributes = True