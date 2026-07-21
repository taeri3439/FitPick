# data

데이터셋 저장 위치. 용량이 크므로 `raw/`, `processed/`는 git에서 제외됨(.gitignore).

```
data/
├── raw/         # 원본 데이터셋 (다운로드)
└── processed/   # 전처리/임베딩 산출물
```

## 후보 데이터셋 (가이드 5번)

- **Polyvore Outfits** (Vasileva et al., Maryland 버전) — compatibility 라벨 포함.
  조화도 학습/평가(FITB, Compatibility AUC)에 바로 활용. **우선 채택.**
  - 원본 Polyvore는 서비스 종료 → 재배포 버전 접근/라이선스 확인 필요.
- **DeepFashion** — 속성/카테고리
- **K-Fashion** (AI Hub) — 한국 패션 특화

`scripts/download_dataset.py`로 내려받아 `raw/`에 배치.
