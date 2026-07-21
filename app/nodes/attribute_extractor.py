"""(확장) VLM 속성 추출 노드.

메타데이터가 없는 옷장 업로드 이미지에서 카테고리/색상/소재 등 속성을 추출한다.
텍스트 LLM 파이프라인과 구조 동일: 프롬프트 지정 → JSON 구조화 출력 → 파싱/재시도.
입력 모달리티만 이미지로 바뀐 것.

기본 그래프(graph.py)에는 포함되지 않음. 이미지 업로드 플로우에서
candidate_filter 앞단에 붙여 사용한다.
"""

from app.state import CodiState


async def attribute_extractor(state: CodiState) -> CodiState:
    # TODO:
    #   1) 업로드 이미지 → VLM 호출 (app.models.vlm_extractor)
    #   2) JSON 구조화 출력 파싱/검증/재시도
    #   3) 추출 속성을 아이템 메타데이터로 저장
    return {
        "trace": ["attribute_extractor: not implemented"],
    }
