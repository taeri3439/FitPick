"""LLM 클라이언트 — 추천 이유 설명 생성 및 TPO 파싱용.

기존 RAG 프로젝트의 LLM 파이프라인을 재사용한다.
"""

from functools import lru_cache

from langchain_openai import ChatOpenAI


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    # TODO: 모델/온도 등 config 연동
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
