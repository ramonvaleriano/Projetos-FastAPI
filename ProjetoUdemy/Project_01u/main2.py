from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


class Usuario(BaseModel):

    id: Optional[int] = None
    nome: str
    senha: str

@app.post('/usuario')
def mostrar_usuario(usuario: Usuario):

    return usuario