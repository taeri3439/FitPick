"""FastAPI 진입점."""

import logging

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from app.routers import recommend  # noqa: E402

logger = logging.getLogger("uvicorn.error")

app = FastAPI(
    title="FitPick",
    description="멀티모달 임베딩 기반 코디 추천 서비스",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
