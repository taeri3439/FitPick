"""의류 아이템 도메인 모델."""

from enum import Enum

from pydantic import BaseModel


class Category(str, Enum):
    TOP = "top"
    BOTTOM = "bottom"
    OUTER = "outer"
    SHOES = "shoes"
    ACC = "acc"


class ClothingItem(BaseModel):
    """옷장 아이템. 임베딩은 Qdrant에 저장하고 여기엔 메타데이터만."""

    id: str
    category: Category
    image_path: str
    color: str | None = None
    material: str | None = None
    style: str | None = None
    season: str | None = None
    # TODO: 필요한 속성 필드 추가
