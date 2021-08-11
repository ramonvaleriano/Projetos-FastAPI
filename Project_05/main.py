from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

from typing import List


app = FastAPI()

class Animal(BaseModel):
    id : Optional[int]
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
    animal.id = uuid4()
    banco.append(animal)

    return {'mensagem':'Animal Adicionado'}