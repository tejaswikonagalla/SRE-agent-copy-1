from fastapi import status
from .client import client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
import os

# Setup the database for testing
DATABASE_URL = "sqlite:///./test.db"

# Create a new database session and return a new connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Run migrations
def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

# Ensure migrations are applied before running tests
run_migrations()

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json == {"ping": "pong"}