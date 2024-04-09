import pytest
import logging

LOGGER = logging.getLogger(__name__)


@pytest.fixture()
def test_category_get(client):
    response = client.get(
        "/category",
    )

    assert response.status_code == 200
    assert response.json == []


@pytest.fixture()
def test_category_create(client):
    response = client.post(
        "/category",
        json={"name": "Test Category"},
    )

    assert response.status_code == 201
    assert response.json["name"] == "Test Category"


@pytest.fixture()
def test_category_create_duplicate_name(client):
    client.post(
        "/category",
        json={"name": "Test Category"},
    )

    response = client.post(
        "/category",
        json={"name": "Test Category"},
    )
    assert response.status_code == 400
    assert response.json["message"] == "A category with that name already exists."


@pytest.fixture()
def test_category_get_single(client):
    client.post(
        "/category",
        json={"name": "Test Category"},
    )

    response = client.get(
        "/category",
    )

    assert response.status_code == 200
    assert response.json == [{"id": 1, "name": "Test Category", "posts": []}]



@pytest.fixture()
def test_category_get_multiple(client):
    client.post(
        "/category",
        json={"name": "Test Category"},
    )
    client.post(
        "/category",
        json={"name": "Test Category 2"},
    )

    response = client.get(
        "/category",
    )

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Test Category"
    assert response.json[1]["name"] == "Test Category 2"


@pytest.fixture()
def test_category_delete(client, admin_jwt, created_category_id):
    response = client.delete(
        f"/category/{created_category_id}",
        headers={"Authorization": f"Bearer {admin_jwt}"},
    )

    assert response.status_code == 200
    assert response.json["message"] == "Category deleted."


@pytest.fixture()
def test_category_delete_without_admin(client, jwt, created_category_id):
    response = client.delete(
        f"/category/{created_category_id}",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == 401
    assert response.json["message"] == "Admin privilege required."

