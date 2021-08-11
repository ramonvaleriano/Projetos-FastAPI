from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from typing import List


app = FastAPI()

class Animal(BaseModel):
    id : int
    nome : str
    idade : int
    sexo : str
    cor : str

banco: List[Animal] = []

@app.get('/animais')
def lista_animais():

    return banco

@app.post('/animais')
def criar_animel(animal: Animal):
    banco.append(animal)

    return {'mensagem':'Animal Adicionado'}