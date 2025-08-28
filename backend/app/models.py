from __future__ import annotations

from datetime import datetime
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, BigInteger, String, DateTime, func, CHAR, UniqueConstraint, Index


class Base(DeclarativeBase):
    pass


# 공통 컬럼 Mixin
class CommonColumns:
    use_tf: Mapped[str] = mapped_column(CHAR(1), nullable=False, default="Y", server_default="Y", comment="사용여부 (Y/N)")
    del_tf: Mapped[str] = mapped_column(CHAR(1), nullable=False, default="N", server_default="N", comment="삭제여부 (Y/N)")

    reg_adm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="등록자")
    reg_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="등록일")

    up_adm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="수정자")
    up_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, onupdate=func.now(), comment="수정일")

    del_adm: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, comment="삭제자")
    del_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True, comment="삭제일")


class User(Base, CommonColumns):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="PK")
    email: Mapped[str] = mapped_column(String(191), nullable=False, unique=True, index=True, comment="이메일")
    password_hash: Mapped[str] = mapped_column(String(191), nullable=False, comment="비밀번호 해시")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="생성 시각")


class Stock(Base, CommonColumns):
    __tablename__ = "stocks"
    __table_args__ = (
        UniqueConstraint("symbol", name="uq_symbol"),
        Index("idx_stocks_market", "market"),
        Index("idx_stocks_sector", "sector"),
    )
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, comment="PK")
    symbol: Mapped[str] = mapped_column(String(20), nullable=False, index=True, comment="종목 코드")
    name: Mapped[str] = mapped_column(String(100), nullable=False, comment="종목명")
    market : Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    sector : Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    tags : Mapped[Optional[str]] = mapped_column(String(255), nullable=True, comment="태그 (콤마로 구분)") 
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now(), comment="생성일")
