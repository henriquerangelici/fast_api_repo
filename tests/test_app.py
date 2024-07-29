from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_olamundo(client):
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'ola mundo'}  # Assert


def test_create_user(client):
    response = client.post(  # User Schema
        '/users/',
        json={
            'username': 'testename',
            'password': 'senha',
            'email': 'teste@teste.com',
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {'username': 'testename', 'email': 'teste@teste.com', 'id': 1}


def test_read_user(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testename',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_update_ser(client):
    response = client.put(
        '/users/1',
        json={'username': 'testename2', 'email': 'teste@teste.com', 'id': 1, 'password': '123'},
    )

    assert response.json() == {
        'username': 'testename2',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'Usuario deletado'}
