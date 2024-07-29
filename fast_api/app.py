from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_api.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # o user vai p/ UserSchema (validação), mas retorno é o UserPublic
    user_id = UserDB(
        id=len(database) + 1,
        **user.model_dump(),  # convert pydantic em dict
    )

    database.append(user_id)

    return user_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{id_user}', response_model=UserPublic)
def update_user(id_user: int, user: UserSchema):
    if id_user < 1 or id_user > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    user_id = UserDB(**user.model_dump(), id=id_user)

    database[id_user - 1] = user_id

    return user_id


@app.delete('/users/{id_user}', response_model=Message)
def delete_user(id_user: int):
    if id_user < 1 or id_user > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado')

    del database[id_user - 1]

    return {'message': 'Usuario deletado'}
