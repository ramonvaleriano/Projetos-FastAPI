from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List

from schemas import schemas
from infra.sqlalchemy.config.database import get_db, criar_banco_de_dados
from infra.sqlalchemy.repositorios.produto import RespositorioProduto

criar_banco_de_dados()

app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.ProdutoSimples)
def adicionar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):

    produto_criado = RespositorioProduto(db).criar(produto)

    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[schemas.ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):

    list_de_produto = RespositorioProduto(db).listar()
    
    return list_de_produto