from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    app_name: str = "Deployment Service API"

    database_url: str

    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Settings()