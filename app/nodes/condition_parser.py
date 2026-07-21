"""① 조건 파싱 노드.

자연어 요청(user_query)에서 날씨/TPO 조건을 추출한다.
- 날씨: 외부 API(기상청/OpenWeather) 호출 or 쿼리에서 파싱
- TPO: LLM으로 구조화 추출 (Time / Place / Occasion)
"""

from app.state import CodiState


async def condition_parser(state: CodiState) -> CodiState:
    # TODO: user_query → weather / tpo 구조화 추출
    #   1) 날씨 API 호출 (app.models.llm_client 또는 별도 weather 유틸)
    #   2) LLM으로 TPO 파싱 → dict
    return {
        "weather": {},
        "tpo": {},
        "trace": ["condition_parser: not implemented"],
    }
