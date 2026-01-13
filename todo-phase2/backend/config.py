import os
from typing import Optional

class Settings:
    """Application settings loaded from environment variables"""

    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./todo.db")
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET", "")
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")

    @property
    def allowed_origins_list(self) -> list:
        """Return allowed origins as a list"""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]

# Create settings instance
settings = Settings()