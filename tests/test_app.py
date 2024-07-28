from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api.app import app


def test_read_root_deve_retornar_ok_e_olamundo():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'ola mundo'}  # Assert
