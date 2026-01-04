from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENV: str = "development"
    RPC_URL: str
    REQUIRED_CONFIRMATIONS: int = 1

    # ADD THESE TWO
    PRIVATE_KEY: str
    SENDER_ADDRESS: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="forbid"
    )


settings = Settings()
