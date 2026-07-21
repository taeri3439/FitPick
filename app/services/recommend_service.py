"""추천 유스케이스 오케스트레이션.

라우터와 LangGraph 파이프라인 사이의 얇은 서비스 레이어.
그래프 실행 → 결과를 API 응답 스키마로 변환.
"""

from app.graph import compiled_graph
from app.schemas.api import RecommendRequest, RecommendResponse


class RecommendService:
    def __init__(self):
        # 체크포인터가 필요하면 compile 시 주입 (graphpath main.py 참고)
        self.agent = compiled_graph.compile()

    async def recommend(self, req: RecommendRequest) -> RecommendResponse:
        result = await self.agent.ainvoke(
            {
                "user_query": req.user_query,
                "wardrobe_item_ids": req.wardrobe_item_ids,
            }
        )
        # TODO: result(recommendations/explanation) → RecommendResponse 매핑
        return RecommendResponse(
            recommendations=[],
            explanation=result.get("explanation", ""),
        )
