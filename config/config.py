import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "CloudOpsPortal@2026")

    # Use DATABASE_URL in production (Render/Neon)
    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:
        # Render/Neon sometimes provide postgres:// instead of postgresql://
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL or (
        f"postgresql://{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:"
        f"{os.getenv('POSTGRES_PORT')}/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False