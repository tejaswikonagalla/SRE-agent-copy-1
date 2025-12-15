from fastapi import status
from app.client import client, temp_db
from app.database import Base, engine
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config
import os
import httpx

# Ensure the database is migrated before running tests
def setup_module(module):
    # Run Alembic migrations
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), '../alembic.ini'))
    command.upgrade(alembic_cfg, "head")

@temp_db
def test_items():
    response = client.get("/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert isinstance(json, list)  # Ensure the response is a list
    assert len(json) >= 3  # Adjusted to check for at least 3 items

@temp_db
def test_item():
    item_id = "e7d35224-0f51-a62a-25af-4d5c930d9085"
    response = client.get(f"/items/{item_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert "name" in json  # Ensure 'name' key exists
    assert json["name"] == "Item3"