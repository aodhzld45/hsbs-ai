# Pydantic 스키마
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

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
    market: Optional[str] = None
    sector: Optional[str] = None
    tags: Optional[str] = None
    use_tf: str
    del_tf: str
    class Config: from_attributes = True
    
class Page(BaseModel):
    total: int
    page: int
    size: int
    items: List[StockOut]