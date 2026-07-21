"""④ 최종 추천 + 설명 생성 노드.

스코어링된 조합(scored_outfits)을 받아 Top-N을 고르고,
LLM으로 "왜 이 조합인지" 추천 이유를 생성한다. (기존 LLM 파이프라인 재사용)
"""

from app.state import CodiState


async def recommender(state: CodiState) -> CodiState:
    # TODO:
    #   1) scored_outfits 상위 N개 선택
    #   2) weather/tpo 컨텍스트 + 조합 정보 → LLM 프롬프트
    #   3) 추천 이유 텍스트 생성 → recommendations / explanation
    return {
        "recommendations": [],
        "explanation": "",
        "trace": ["recommender: not implemented"],
    }
