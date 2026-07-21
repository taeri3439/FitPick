"""코디 추천 API 라우터."""

from fastapi import APIRouter

from app.schemas.api import RecommendRequest, RecommendResponse
from app.services.recommend_service import RecommendService

router = APIRouter(prefix="/recommend", tags=["recommend"])

_service = RecommendService()


@router.post("", response_model=RecommendResponse)
async def recommend(req: RecommendRequest) -> RecommendResponse:
    """자연어 요청 + 옷장 아이템 → 코디 추천."""
    return await _service.recommend(req)
