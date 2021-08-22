from pydantic import BaseModel
from typing import Optional


class PessoaSC(BaseModel):

    id: int
    nome: str
    usuario: str
    senha: str

    class Config:
        orm_mode = True
