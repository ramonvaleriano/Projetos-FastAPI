from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()


class Usuario(BaseModel):

    id: Optional[int] = None
    nome: str
    senha: str

class UsuarioRetorno(BaseModel):

    id: Optional[int] = None
    nome: str

lista = [
    Usuario(id=1, nome='caio', senha='minhasenha1'),
    Usuario(id=2, nome='milaa', senha='minhasenha2'),
    Usuario(id=3, nome='roiroi', senha='minhasenha3')
]

@app.get('/usuariounico', status_code=status.HTTP_202_ACCEPTED, response_model=UsuarioRetorno)
def mostrar_usuario(usuario: Usuario):

    return usuario


@app.get('/usuario', status_code=status.HTTP_200_OK, response_model=List[UsuarioRetorno])
def listar_usuario():

    return lista


@app.post('/usuario', status_code=status.HTTP_201_CREATED, response_model=List[UsuarioRetorno])
def adicionar_usuario(usuario: Usuario):

    lista.append(usuario)

    return lista