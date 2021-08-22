from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from fastapi import FastAPI, status
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from secrets import token_hex

from models.models import Base, Pessoa, Tokens, Session, engine
from scheams.scheams import PessoaSC

app = FastAPI()

def conectaBanco():
    return Session()

@app.post('/cadastro', status_code=status.HTTP_201_CREATED)
def cadastro(nome: str, usuario: str, senha: str):

    session = conectaBanco()
    usuario_coletado = session.query(Pessoa).filter_by(usuario=usuario).all()
    novo_usuario = None

    if len(usuario_coletado) == 0:

        novo_usuario = Pessoa(
            nome=nome,
            usuario=usuario, senha=senha
        )

        session.add(novo_usuario)
        session.commit()

        mensagem = f'Usuaŕio {usuario} cadastrado com sucesso!'

    elif len(usuario_coletado) > 0:
        mensagem = f'Usuário já se encontra Cadastrado!'

    return {
        'mensagem': mensagem
    }

@app.post('/login')
def login(usuario: str, senha: str):
    session = conectaBanco()
    usuario_test = session.query(Pessoa).filter_by(usuario=usuario, senha=senha).all()

    if len(usuario_test) == 0:
        mensagem = f'Usuário inexistente!'
        return {
            'mensagem': mensagem
        }

    token = None
    while True:
        token = token_hex(50)
        tokenExiste = session.query(Tokens).filter_by(token=token).all()

        if len(tokenExiste) == 0:
            pessoaExiste = session.query(Tokens).filter_by(id_pessoa=usuario_test[0].id).all()

            if len(pessoaExiste) == 0:
                novoToken = Tokens(id_pessoa=usuario_test[0].id, token=token)
                session.add(novoToken)

            elif len(pessoaExiste) > 0:
                pessoaExiste[0].token = token

            session.commit()
            break

    mensagem = f'O token é: {token}'

    return {
        'mensagem': token
    }

@app.get('/usuarios')
def usuarios_cadastrados():
    session = conectaBanco()
    usuarios_listados = session.query(Pessoa).all()

    return usuarios_listados