from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas import schemas
from infra.sqlalchemy.config.database import get_db, criar_banco_de_dados
from infra.sqlalchemy.repositorios.produto import RespositorioProduto

criar_banco_de_dados()

app = FastAPI()


@app.post('/produtos')
def adicionar_produto(produto: schemas.Produto, db: Session = Depends(get_db)):

    produto_criado = RespositorioProduto(db).criar(produto)

    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_db)):

    list_de_produto = RespositorioProduto(db).listar()
    
    return list_de_produto