from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


app = FastAPI()

class Todo(BaseModel):

    tarefas: str
    realizada: bool
    prazo: Optional[date]


class TodoSimples(BaseModel):
    tarefas: str
    realizada: bool


lista = list()


@app.post('/inserir', status_code=status.HTTP_201_CREATED, response_model=TodoSimples)
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return todo
    except:
        return {'mensagem':'Não deu certo'}


@app.get('/inserir', status_code=status.HTTP_200_OK, response_model=List[TodoSimples])
def listar():

    return lista


@app.post('/opcao', status_code=status.HTTP_207_MULTI_STATUS)
def lista_opcional(option: int):
    if option == 0:
        return lista
    elif option == 1:
        return list(filter(lambda x: x.realizada == False, lista))
    elif option == 2:
        return list(filter(lambda x: x.realizada == True, lista))
    else:
        return lista[-1]


@app.get('/obter/{user_id}', status_code=status.HTTP_200_OK)
def obter_usuario(user_id: int):
    try:
        return lista[user_id]
    except:
        return {'mensage':'Tarefa não encontrada!'}


@app.post('/alterar/')
def alterar_status(id: int, status: bool):
    try:
        lista[id].realizada = status
        return lista[id]
    except:
        return {'mensagem':'Alteração não permitida.'}


@app.delete('/deletar')
def deletar_usuario(id: int):

    try:
        retorno = lista.pop(id)
        mensagem = f'{retorno} deletado com sucesso!'
    except:
        mensagem = 'Falha ao deletar'

    return {'mensagem':mensagem}