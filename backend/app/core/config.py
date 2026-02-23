from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "OpenSight"
    DATABASE_URL: str = "sqlite:///./data.db"
    SECRET_KEY: str = "your-secret-key-change-me"
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "INFO"
    
    # Google Sheets (optional)
    GOOGLE_SHEETS_CREDENTIALS: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
