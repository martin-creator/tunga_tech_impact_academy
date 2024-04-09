import pytest

@pytest.fixture()
def fresh_jwt(client):
    response = client.post(
        "/auth",
        json={"username": "test", "password": "test"},
    )

    return response.json["access_token"]


@pytest.fixture()
def jwt(client, fresh_jwt):
    response = client.post(
        "/refresh",
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    return response.json["access_token"]


@pytest.fixture()
def created_post_id(client, fresh_jwt):
    response = client.post(
        "/post",
        json={"title": "Test Post", "content": "Test Content"},
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    return response.json["id"]


@pytest.fixture()
def created_store_id(client):
    response = client.post(
        "/store",
        json={"name": "Test Store"},
    )

    return response.json["id"]


@pytest.fixture()
def created_item_id(client, fresh_jwt, created_store_id):
    response = client.post(
        "/item",
        json={"name": "Test Item", "price": 10.5, "store_id": created_store_id},
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    return response.json["id"]


@pytest.fixture()
def created_tag_id(client, created_store_id):
    response = client.post(
        f"/store/{created_store_id}/tag",
        json={"name": "Test Tag"},
    )

    return response.json["id"]


@pytest.fixture()
def created_category_id(client):
    response = client.post(
        "/category",
        json={"name": "Test Category"},
    )

    return response.json["id"]


@pytest.fixture()
def created_user_details(client):
    response = client.post(
        "/user",
        json={"username": "test", "password": "test"},
    )

    return response.json["username"], response.json["password"]

@pytest.fixture()
def created_user_jwts(client):
    response = client.post(
        "/user",
        json={"username": "test", "password": "test"},
    )

    access_token = response.json["access_token"]

    return access_token, access_token

@pytest.fixture()
def admin_jwt(client):
    response = client.post(
        "/auth",
        json={"username": "admin", "password": "admin"},
    )

    return response.json["access_token"]


@pytest.fixture()
def created_author_id(client):
    response = client.post(
        "/author",
        json={"name": "Test Author"},
    )

    return response.json["id"]



# the confest file is used to share fixtures across multiple test files
# fixtures are functions that run before the test functions
