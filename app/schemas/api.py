"""API 요청/응답 모델."""

from pydantic import BaseModel


class RecommendRequest(BaseModel):
    user_query: str
    wardrobe_item_ids: list[str] = []


class OutfitRecommendation(BaseModel):
    outfit_item_ids: list[str]
    score: float
    reason: str


class RecommendResponse(BaseModel):
    recommendations: list[OutfitRecommendation]
    explanation: str
