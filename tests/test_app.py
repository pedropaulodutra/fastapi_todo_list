from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_list.app import app


def test_root_returns_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK


def test_root_returns_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}


def test_home_page_return_200():
    client = TestClient(app)

    response = client.get('/home')

    assert response.status_code == HTTPStatus.OK


def test_home_page_has_hello_world_text():
    client = TestClient(app)

    response = client.get('/home')

    assert 'Hello World!' in response.text
