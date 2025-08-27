# 종목 CRUD (JWT 필요)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..deps import get_db, get_current_user_id
from ..models import Stock
from ..schemas import StockCreate, StockUpdate, StockOut

router = APIRouter(prefix="/stocks", tags=["stocks"])

@router.get("", response_model=List[StockOut])
def list_stocks(db: Session = Depends(get_db), uid: int = Depends(get_current_user_id)):
    return db.query(Stock).order_by(Stock.symbol).all()

@router.post("", response_model=StockOut)
def create_stock(b: StockCreate, db: Session = Depends(get_db), uid: int = Depends(get_current_user_id)):
    if db.query(Stock).filter(Stock.symbol == b.symbol).first():
        raise HTTPException(400, "Symbol exists")
    s = Stock(symbol=b.symbol, name=b.name)
    db.add(s); db.commit(); db.refresh(s)
    return s

@router.put("/{sid}", response_model=StockOut)
def update_stock(sid: int, b: StockUpdate, db: Session = Depends(get_db), uid: int = Depends(get_current_user_id)):
    s = db.get(Stock, sid)
    if not s: raise HTTPException(404, "Not found")
    s.name = b.name
    db.commit(); db.refresh(s)
    return s

@router.delete("/{sid}")
def delete_stock(sid: int, db: Session = Depends(get_db), uid: int = Depends(get_current_user_id)):
    s = db.get(Stock, sid)
    if not s: raise HTTPException(404, "Not found")
    db.delete(s); db.commit()
    return {"ok": True}
