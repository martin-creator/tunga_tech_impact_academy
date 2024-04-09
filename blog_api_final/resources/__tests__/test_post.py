
def test_create_post(client, fresh_jwt):
    response = client.post(
        "/post",
        json={"title": "Test Post", "content": "Test Content"},
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    assert response.status_code == 201
    assert response.json["title"] == "Test Post"
    assert response.json["content"] == "Test Content"




def test_create_post_with_unknown_data(client, fresh_jwt):
    response = client.post(
        "/post",
        json={
            "title": "Test Post",
            "content": "Test Content",
            "unknown_field": "unknown",
        },
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    assert response.status_code == 422
    assert response.json["errors"]["json"]["unknown_field"] == ["Unknown field."]



def test_create_post_with_non_fresh_jwt(client, jwt):
    response = client.post(
        "/post",
        json={"title": "Test Post", "content": "Test Content"},
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == 401
    assert response.json == {
        "description": "The token is not fresh.",
        "error": "fresh_token_required",
    }



def test_delete_post(client, admin_jwt, created_post_id):
    response = client.delete(
        f"/post/{created_post_id}",
        headers={"Authorization": f"Bearer {admin_jwt}"},
    )

    assert response.status_code == 200
    assert response.json["message"] == "Post deleted."


def test_delete_post_without_admin(client, jwt, created_post_id):
    response = client.delete(
        f"/post/{created_post_id}",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == 401
    assert response.json["message"] == "Admin privilege required."



def test_update_post(client, jwt, created_post_id):
    response = client.put(
        f"/post/{created_post_id}",
        json={"title": "Test Post (updated)", "content": "Test Content"},
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == 200
    assert response.json["title"] == "Test Post (updated)"
    assert response.json["content"] == "Test Content"


def test_get_all_posts(client, fresh_jwt, jwt):
    response = client.post(
        "/post",
        json={"title": "Test Post", "content": "Test Content"},
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )
    response = client.post(
        "/post",
        json={"title": "Test Post 2", "content": "Test Content"},
        headers={"Authorization": f"Bearer {fresh_jwt}"},
    )

    response = client.get(
        "/post",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["title"] == "Test Post"
    assert response.json[0]["content"] == "Test Content"
    assert response.json[1]["title"] == "Test Post 2"











