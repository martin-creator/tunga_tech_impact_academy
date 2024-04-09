def test_author_get(client):
    response = client.get(
        "/author",
    )

    assert response.status_code == 200
    assert response.json == []


def test_author_create(client):
    response = client.post(
        "/author",
        json={"name": "Test Author"},
    )

    assert response.status_code == 201
    assert response.json["name"] == "Test Author"


def test_author_create_duplicate_name(client):
    client.post(
        "/author",
        json={"name": "Test Author"},
    )

    response = client.post(
        "/author",
        json={"name": "Test Author"},
    )
    assert response.status_code == 400
    assert response.json["message"] == "An author with that name already exists."


def test_author_get_single(client):
    client.post(
        "/author",
        json={"name": "Test Author"},
    )

    response = client.get(
        "/author",
    )

    assert response.status_code == 200
    assert response.json == [{"id": 1, "name": "Test Author", "posts": []}]


def test_author_get_multiple(client):
    client.post(
        "/author",
        json={"name": "Test Author"},
    )
    client.post(
        "/author",
        json={"name": "Test Author 2"},
    )

    response = client.get(
        "/author",
    )

    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "name": "Test Author", "posts": []},
        {"id": 2, "name": "Test Author 2", "posts": []},
    ]








