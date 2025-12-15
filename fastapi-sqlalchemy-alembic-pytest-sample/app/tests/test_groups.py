from fastapi import status
from app.tests.client import client, temp_db
from app.models import Group, Item  # Ensure these imports are correct based on your repo structure

# Ensure the correct import path for client and temp_db
# Assuming the correct path is app.tests.client

@temp_db
def test_groups():
    # Setup initial data
    Group.create(name="Group1", description="Group1 description")
    Group.create(name="Group2", description="Group2 description")

    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group():
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    Group.create(id=group_id, name="Group2", description="Group2 description")

    response = client.get(f"/groups/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1():
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    # Setup initial data
    group = Group.create(id=group_id, name="Group1", description="Group1 description")
    Item.create(name="Item1", group_id=group.id)
    Item.create(name="Item2", group_id=group.id)

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2():
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    # Setup initial data
    group = Group.create(id=group_id, name="Group2", description="Group2 description")
    Item.create(name="Item3", group_id=group.id)

    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1