"""③ 조화도 스코어링 노드 (프로젝트의 핵심 학습 축).

후보 아이템들의 이미지 임베딩을 기반으로 코디 조합의 '조화도'를 스코어링한다.

주의(가이드 8번 참고):
    CLIP 코사인 유사도 = "비슷한 것"이지 "잘 어울리는 것"이 아니다.
    Polyvore compatibility 라벨로 학습한 조화도 모델(type-aware embedding,
    outfit compatibility)을 별도로 두는 것을 권장.
    → 여기서는 그 스코어러를 호출해 조합별 점수를 만든다.
"""

from app.state import CodiState


async def harmony_scorer(state: CodiState) -> CodiState:
    # TODO:
    #   1) candidate_item_ids 임베딩 조회 (app.vectorstore)
    #   2) 조합 후보 생성 (상의/하의/아우터/신발 ...)
    #   3) 조화도 스코어 계산 (app.models.clip_embedder + compatibility 로직)
    #   4) 상위 조합 → scored_outfits
    return {
        "scored_outfits": [],
        "trace": ["harmony_scorer: not implemented"],
    }
