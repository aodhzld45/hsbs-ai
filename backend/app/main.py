# 엔트리(라우터 등록만)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CORS_ORIGINS
from .db import engine
from .models import Base
from .schemas import HealthOut
from .routers import auth_router, stocks_router

app = FastAPI(title="HSBS AI Proto (modular)")

if CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 테이블 생성(간단용)
Base.metadata.create_all(bind=engine)

@app.get("/health", response_model=HealthOut)
def health():
    return {"ok": True}

# 라우터 등록
app.include_router(auth_router.router)
app.include_router(stocks_router.router)
