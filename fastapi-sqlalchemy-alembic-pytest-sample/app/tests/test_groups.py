from fastapi import status
from .client import client, temp_db  # Adjusted import path for client and temp_db
from ..models import Group, Item  # Adjusted import path for Group and Item
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text

@temp_db
def test_groups(db: Session):
    # Setup initial data
    try:
        db.execute(text("INSERT INTO groups (id, name, description) VALUES ('1', 'Group1', 'Group1 description')"))
        db.execute(text("INSERT INTO groups (id, name, description) VALUES ('2', 'Group2', 'Group2 description')"))
        db.commit()
    except IntegrityError:
        db.rollback()

    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group(db: Session):
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    try:
        db.execute(text(f"INSERT INTO groups (id, name, description) VALUES ('{group_id}', 'Group2', 'Group2 description')"))
        db.commit()
    except IntegrityError:
        db.rollback()

    response = client.get(f"/groups/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1(db: Session):
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    # Setup initial data
    try:
        db.execute(text(f"INSERT INTO groups (id, name, description) VALUES ('{group_id}', 'Group1', 'Group1 description')"))
        db.execute(text(f"INSERT INTO items (name, group_id) VALUES ('Item1', '{group_id}')"))
        db.execute(text(f"INSERT INTO items (name, group_id) VALUES ('Item2', '{group_id}')"))
        db.commit()
    except IntegrityError:
        db.rollback()

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2(db: Session):
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    try:
        db.execute(text(f"INSERT INTO groups (id, name, description) VALUES ('{group_id}', 'Group2', 'Group2 description')"))
        db.execute(text(f"INSERT INTO items (name, group_id) VALUES ('Item3', '{group_id}')"))
        db.commit()
    except IntegrityError:
        db.rollback()

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1