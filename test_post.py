import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post_status():
    data = {"title": "My first post", "body": "Learning API testing", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201


def test_create_post_returns_same_data():
    data = {"title": "My first post", "body": "Learning API testing", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.json()["title"] == "My first post"
    assert response.json()["userId"] == 1


def test_create_post_has_id():
    data = {"title": "My first post", "body": "Learning API testing", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert "id" in response.json()