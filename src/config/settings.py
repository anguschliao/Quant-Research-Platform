from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # =========================
    # OANDA
    # =========================
    oanda_api_key: str = Field(default="")
    oanda_account_id: str = Field(default="")
    oanda_env: str = Field(default="practice")
    oanda_api_url: str = Field(default="")

    # =========================
    # Optional Data Providers
    # =========================
    polygon_api_key: str = Field(default="")
    alphavantage_api_key: str = Field(default="")
    finnhub_api_key: str = Field(default="")
    fred_api_key: str = Field(default="")
    newsapi_api_key: str = Field(default="")

    # =========================
    # Database
    # =========================
    database_url: str = Field(default="")

    # =========================
    # Logging
    # =========================
    log_level: str = Field(default="INFO")

    # =========================
    # Development
    # =========================
    random_seed: int = Field(default=42)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()