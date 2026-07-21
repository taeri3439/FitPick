"""LangGraph 코디 추천 파이프라인의 상태 정의.

각 노드는 이 State의 일부 필드를 읽고, 자신이 채운 필드만 반환한다.
(graphpath 프로젝트의 AgentState 패턴을 따름)
"""

from typing import Annotated, TypedDict


def append_to_list(existing: list, new: list) -> list:
    """리스트 필드 누적용 reducer."""
    return existing + new


class CodiState(TypedDict, total=False):
    # ── 입력 ──
    user_query: str            # 자연어 요청 (예: "내일 비 오는데 소개팅 코디")
    wardrobe_item_ids: list[str]  # 후보로 삼을 사용자 옷장 아이템 id 목록

    # ── ① 조건 파싱 결과 ──
    weather: dict              # {"temp": .., "condition": "rain", ...}
    tpo: dict                  # {"time": .., "place": .., "occasion": ..}

    # ── ② 후보 필터링 결과 ──
    candidate_item_ids: list[str]

    # ── ③ 조화도 스코어링 결과 ──
    # [{"outfit": [item_id, ...], "score": 0.87}, ...]
    scored_outfits: list[dict]

    # ── ④ 최종 추천 ──
    recommendations: list[dict]  # Top-N 코디 + 추천 이유
    explanation: str

    # ── 로그/디버깅 ──
    trace: Annotated[list[str], append_to_list]
