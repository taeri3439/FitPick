"""CLIP / FashionCLIP 이미지·텍스트 임베딩 래퍼.

이 프로젝트의 '새로 배우는 축'. 이미지를 벡터로 변환해 Qdrant에 저장하고,
조화도 스코어링(harmony_scorer)에서 사용한다.
"""

from functools import lru_cache

from app.config import get_settings


class ClipEmbedder:
    """CLIP 계열 모델 로딩 + 임베딩 인터페이스."""

    def __init__(self, model_name: str):
        self.model_name = model_name
        # TODO: transformers/open_clip로 모델·프로세서 로드
        self.model = None
        self.processor = None

    def embed_image(self, image) -> list[float]:
        """PIL 이미지 → 임베딩 벡터."""
        # TODO: 이미지 전처리 → model.get_image_features → normalize
        raise NotImplementedError

    def embed_text(self, text: str) -> list[float]:
        """텍스트 → 임베딩 벡터 (텍스트 쿼리 검색용)."""
        # TODO: tokenize → model.get_text_features → normalize
        raise NotImplementedError


@lru_cache(maxsize=1)
def get_embedder() -> ClipEmbedder:
    return ClipEmbedder(get_settings().clip_model_name)
