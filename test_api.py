import requests
import pytest
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_status_code():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200


def test_user_name():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json()["name"] == "Leanne Graham"


def test_user_city():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json()["address"]["city"] == "Gwenborough"


@pytest.mark.parametrize("user_id, expected_status",[
    (1, 200),
    (10, 200),
    (11, 404),
    (101, 404),
])
def test_user_status(user_id, expected_status):
    response=requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code==expected_status