```python
from fastapi import status
from app.tests.client import client


def test_root():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK

    json = response.json()
    assert json == {"ping": "pong"}
```