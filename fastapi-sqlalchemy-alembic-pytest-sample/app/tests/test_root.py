from fastapi import status
from app.tests.client import client
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

# Assuming the database URL is defined somewhere in the app
DATABASE_URL = "sqlite:///./test.db"

# Create a new database session for the test
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Drop all tables in the test database to ensure a clean state
Base.metadata.drop_all(bind=engine)
# Create all tables in the test database
Base.metadata.create_all(bind=engine)

def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json == {"ping": "pong"}