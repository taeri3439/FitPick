"""앱 전역 설정. .env 값을 로드해 각 모듈에서 참조한다."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    openai_api_key: str = ""

    # Qdrant
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str = ""
    qdrant_collection: str = "fitpick_items"

    # 임베딩 / VLM
    clip_model_name: str = "patrickjohncyh/fashion-clip"
    vlm_model_name: str = ""

    # 외부 API
    weather_api_key: str = ""

    # 앱
    log_level: str = "INFO"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
