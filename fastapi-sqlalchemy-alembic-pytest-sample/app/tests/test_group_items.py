from fastapi import status
from app.tests.utils import client, temp_db  # Adjusted import path

@temp_db
def test_group_items():
    response = client.get("/group_items")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert isinstance(json, list)  # Ensure the response is a list
    assert len(json) == 3

@temp_db
def test_group_item():
    group_id = "7d60e1d4-a6af-fc52-6355-67c3094479ab"  # Corrected group_id
    response = client.get(f"/group_items/{group_id}")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert isinstance(json, dict)  # Ensure the response is a dictionary
    assert json["group_id"] == "7d60e1d4-a6af-fc52-6355-67c3094479ab"
    assert json["item_id"] == "9ab921a1-d177-7691-0bb4-b66ef823d9b4"