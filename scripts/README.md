# scripts

파이프라인과 별개로 실행하는 유틸 스크립트.

| 스크립트 | 역할 |
|----------|------|
| `download_dataset.py` | 데이터셋 다운로드 → `data/raw/` |
| `build_index.py` | 이미지 임베딩(CLIP) → Qdrant 인덱싱 |

실행 예: `python -m scripts.build_index`
