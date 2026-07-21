"""(확장) 생성형 VLM 래퍼 — 이미지 속성 추출용.

CLIP(임베딩)과는 다른 카테고리. 이미지+프롬프트 → 구조화된 텍스트(JSON) 생성.
Qwen-VL / LLaVA / Claude Vision 등.
"""

from functools import lru_cache

from app.config import get_settings


class VlmExtractor:
    def __init__(self, model_name: str):
        self.model_name = model_name
        # TODO: VLM 클라이언트/모델 초기화

    async def extract_attributes(self, image) -> dict:
        """이미지 → {카테고리, 색상, 소재, 핏, 스타일 ...} JSON."""
        # TODO: 프롬프트 지정 → 생성 → JSON 파싱/검증/재시도
        raise NotImplementedError


@lru_cache(maxsize=1)
def get_vlm() -> VlmExtractor:
    return VlmExtractor(get_settings().vlm_model_name)
