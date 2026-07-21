"""이미지 임베딩 → Qdrant 인덱싱 스크립트.

data/ 의 아이템 이미지를 CLIP으로 임베딩해 Qdrant 컬렉션에 적재한다.
harmony_scorer가 검색·스코어링에 사용.
"""

from app.models.clip_embedder import get_embedder
from app.vectorstore import qdrant_store


def main() -> None:
    embedder = get_embedder()  # noqa: F841
    # TODO:
    #   1) qdrant_store.ensure_collection(vector_size)
    #   2) 이미지 순회 → embedder.embed_image → points 구성
    #   3) qdrant_store.upsert_items(points)
    raise NotImplementedError


if __name__ == "__main__":
    main()
