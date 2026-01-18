import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings loaded from environment variables"""

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("ERROR: DATABASE_URL is missing! Check your .env file.")
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET")
    if not BETTER_AUTH_SECRET:
        print("WARNING: BETTER_AUTH_SECRET is not set!")
    ALLOWED_ORIGINS: str = os.getenv(
        "ALLOWED_ORIGINS", 
        "https://todo-mujahidshaikh81.vercel.app,http://localhost:3000,http://127.0.0.1:3001")

    @property
    def allowed_origins_list(self) -> list:
        
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]

# Create settings instance
settings = Settings()