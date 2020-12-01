from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = True
    ALLOOW_CREDENTIALS: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    LOG_LEVEL: str = "info"
    PROJECT_NAME: str = 'I.A.'
    API_V1_STR: str = '/api/v1'
    ORIGINS: str = "http://localhost:8080"

    class Config:
        env_file: str = '.env'


settings = Settings()
