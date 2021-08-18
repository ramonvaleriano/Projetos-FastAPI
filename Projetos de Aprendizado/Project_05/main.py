from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

from typing import List


app = FastAPI()

class Animal(BaseModel):
    id : Optional[str]
    nome : str
    idade : int
    sexo : str
    cor : str

banco: List[Animal] = []

@app.get('/animais')
def lista_animais():

    return banco


@app.get('/animais/{animdal_id}')
def obter_animal(animdal_id: str):
    for animal in banco:
        if animal.id == animdal_id:
            return animal

    return {'mensagem': 'Animal não localizado'}


@app.post('/animais')
def criar_animel(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)

    return {'mensagem':'Animal Adicionado'}


@app.delete('/animais/{animal_id}')
def removendo_animal(animal_id: str):
    posicao = None
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    
    if posicao:
        animal_removido = banco.pop(posicao)
        return {'mensagem':animal_removido}

    return {'mensagem': 'Animal não foi encontrado.'}