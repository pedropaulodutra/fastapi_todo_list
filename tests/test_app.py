from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_list.app import app


def test_root_should_return_hello_world_and_return_200():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello World!'}
    assert response.status_code == HTTPStatus.OK
