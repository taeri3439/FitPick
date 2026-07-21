"""Qdrant 벡터 스토어 연동.

기존 RAG 프로젝트에서 텍스트 임베딩에 쓰던 Qdrant를,
여기서는 옷 이미지 임베딩 저장/검색에 재활용한다.
"""

from functools import lru_cache

from qdrant_client import QdrantClient

from app.config import get_settings


@lru_cache(maxsize=1)
def get_client() -> QdrantClient:
    s = get_settings()
    return QdrantClient(url=s.qdrant_url, api_key=s.qdrant_api_key or None)


def ensure_collection(vector_size: int) -> None:
    """컬렉션이 없으면 생성한다."""
    # TODO: recreate_collection / create_collection (Cosine distance)
    raise NotImplementedError


def upsert_items(points: list[dict]) -> None:
    """아이템 임베딩 + 메타데이터 저장."""
    # TODO: client.upsert(collection, points)
    raise NotImplementedError


def search(vector: list[float], top_k: int = 20, query_filter=None) -> list[dict]:
    """벡터 검색 (메타데이터 필터 지원)."""
    # TODO: client.search(...)
    raise NotImplementedError
