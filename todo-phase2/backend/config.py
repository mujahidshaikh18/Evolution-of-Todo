<<<<<<< HEAD
import sys
import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()
=======
import os
from typing import Optional
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09

class Settings:
    """Application settings loaded from environment variables"""

<<<<<<< HEAD
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("ERROR: DATABASE_URL is missing! Check your .env file.")
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET")
    if not BETTER_AUTH_SECRET:
        print("WARNING: BETTER_AUTH_SECRET is not set!")
    ALLOWED_ORIGINS: str = os.getenv(
        "ALLOWED_ORIGINS",
        "https://todo-mujahidshaikh81.vercel.app,http://localhost:3000,http://127.0.0.1:3001")

    # Cohere Configuration
    COHERE_API_KEY: str = os.getenv("COHERE_API_KEY")
    if not COHERE_API_KEY:
        print("WARNING: COHERE_API_KEY is not set!")
    COHERE_MODEL: str = os.getenv("COHERE_MODEL", "command-r-8-2024")

    @property
    def allowed_origins_list(self) -> list:

=======
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./todo.db")
    BETTER_AUTH_SECRET: str = os.getenv("BETTER_AUTH_SECRET", "")
    ALLOWED_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")

    @property
    def allowed_origins_list(self) -> list:
        """Return allowed origins as a list"""
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",") if origin.strip()]

# Create settings instance
settings = Settings()