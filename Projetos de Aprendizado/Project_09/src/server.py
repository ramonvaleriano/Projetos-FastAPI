from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import schema
from schemas.schemas import Produto, ProdutoSimples, Usuario
from infra.sqlalchemy.config.database import get_db, criar_bd
from infra.sqlalchemy.repositorios.produto import RepositorioProduto
from infra.sqlalchemy.repositorios.usuario import RepositorioUsuario

#criar_bd()

app = FastAPI()


# Rotas de Produtos
@app.post('/produtos', status_code=status.HTTP_200_OK, response_model=ProdutoSimples)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    
    produto_criado = RepositorioProduto(db).criar(produto)
    
    return produto_criado


@app.get('/produtos', status_code=status.HTTP_201_CREATED)
def listar_produtos(db: Session = Depends(get_db)):
    
    produtos = RepositorioProduto(db).listar()
    
    return produtos


# Rodas de Usuários
@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    
    usuario_criado = RepositorioUsuario(session).criar(usuario)

    return usuario_criado


@app.get('/usuarios', status_code=status.HTTP_200_OK, response_model=Usuario)
def listar_usuarios():
    pass
