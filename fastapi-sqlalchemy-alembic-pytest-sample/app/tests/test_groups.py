from fastapi import status
from .client import client, temp_db  # Adjusted import path for client and temp_db
from ..models import Group, Item  # Adjusted import path for Group and Item
from sqlalchemy.orm import Session

@temp_db
def test_groups(db: Session):
    # Setup initial data
    db.add(Group(id="1", name="Group1", description="Group1 description"))
    db.add(Group(id="2", name="Group2", description="Group2 description"))
    db.commit()

    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group(db: Session):
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    db.add(Group(id=group_id, name="Group2", description="Group2 description"))
    db.commit()

    response = client.get(f"/groups/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1(db: Session):
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    # Setup initial data
    group = Group(id=group_id, name="Group1", description="Group1 description")
    db.add(group)
    db.add(Item(name="Item1", group_id=group.id))
    db.add(Item(name="Item2", group_id=group.id))
    db.commit()

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2(db: Session):
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    group = Group(id=group_id, name="Group2", description="Group2 description")
    db.add(group)
    db.add(Item(name="Item3", group_id=group.id))
    db.commit()

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1