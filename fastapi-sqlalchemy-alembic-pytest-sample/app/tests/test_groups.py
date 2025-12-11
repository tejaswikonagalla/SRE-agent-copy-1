from fastapi import status

from app.tests.client import client, temp_db
from app.models import Group, Item  # Assuming these are the correct models

# Assuming a function to populate the database with test data
def populate_test_data():
    group1 = Group(id="7d60e1d4-a6af-fc52-6355-67c3094479ab", name="Group1", description="Group1 description")
    group2 = Group(id="218587ed-d548-bd06-d278-43583021c1a9", name="Group2", description="Group2 description")
    item1 = Item(id="item1", name="Item1", group_id=group1.id)
    item2 = Item(id="item2", name="Item2", group_id=group1.id)
    item3 = Item(id="item3", name="Item3", group_id=group2.id)
    
    # Assuming a session object is available for database operations
    session.add_all([group1, group2, item1, item2, item3])
    session.commit()

@temp_db
def test_groups():
    populate_test_data()  # Populate test data before running the test
    response = client.get("/groups")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group():
    populate_test_data()  # Populate test data before running the test
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    response = client.get(f"/groups/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json["name"] == "Group2"
    assert json["description"] == "Group2 description"

@temp_db
def test_group_items_1():
    populate_test_data()  # Populate test data before running the test
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 2

@temp_db
def test_group_items_2():
    populate_test_data()  # Populate test data before running the test
    group_id = "218587ed-d548-bd06-d278-43583021c1a9"
    response = client.get(f"/groups/{group_id}/items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert len(json) == 1