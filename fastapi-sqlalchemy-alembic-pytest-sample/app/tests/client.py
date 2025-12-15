from fastapi import Header, HTTPException, status
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.dependencies import get_database
from app.main import app
from app.models import Base  # Assuming models.py contains SQLAlchemy models and Base

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables in the in-memory database
Base.metadata.create_all(bind=engine)

def temp_db(f):
    def func(*args, **kwargs):
        def override_get_db():
            db = TestingSessionLocal()
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_database] = override_get_db
        try:
            return f(*args, **kwargs)
        finally:
            app.dependency_overrides[get_database] = get_database

    return func

client = TestClient(app)