import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

# Ensure the environment variable is loaded
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

# Parse the database URL to ensure it's correctly formatted
try:
    SQLALCHEMY_DATABASE_URL = URL.create(DATABASE_URL)
except Exception as e:
    raise RuntimeError(f"Invalid DATABASE_URL format: {e}")

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()