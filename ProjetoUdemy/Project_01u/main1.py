from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

lista = [
    (1, 'caio', 'minhasenha1'),
    (2, 'joao', 'minhasenha2')
]

@app.get('/usuario/{id}')
def main(id: int):

    mensagem = f'O meu id {id}'

    for index, valor in enumerate(lista):
        print(valor[0])
        if valor[0] == id:
            mensagem = f'Encontrou usuário {valor}'
        else:
            mensagem = 'Não encontrou usuário desejado!'

    return {
        'mensagem': mensagem
    }

@app.post('/usuario/')
def usuariopost(nome):

    for index, valor in enumerate(lista):
        print(valor[1])
        if valor[1] == nome:
            mensagem = f'Encontrou usuário {valor}'
        else:
            mensagem = 'Não encontrou usuário desejado!'

    return {
        'mensagem': mensagem,
        'lista': lista
    }