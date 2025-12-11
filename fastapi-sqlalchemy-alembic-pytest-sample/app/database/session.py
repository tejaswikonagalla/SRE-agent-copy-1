import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ensure the environment variable is loaded
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()