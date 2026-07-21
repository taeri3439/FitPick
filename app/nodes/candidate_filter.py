"""② 후보 필터링 노드.

날씨/TPO 조건으로 옷장 아이템의 메타데이터를 필터링해 후보군을 좁힌다.
(임베딩 스코어링 전에 계산량을 줄이는 단계)
"""

from app.state import CodiState


async def candidate_filter(state: CodiState) -> CodiState:
    # TODO: weather/tpo 조건 + wardrobe_item_ids →
    #   메타데이터 규칙 필터링(예: 기온<5 → 반팔 제외) → candidate_item_ids
    return {
        "candidate_item_ids": state.get("wardrobe_item_ids", []),
        "trace": ["candidate_filter: not implemented"],
    }
