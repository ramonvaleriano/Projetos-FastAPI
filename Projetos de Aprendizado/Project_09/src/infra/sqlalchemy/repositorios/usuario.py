from schemas import schemas
from infra.sqlalchemy.models import models

from sqlalchemy.orm import Session
from sqlalchemy import select


class RepositorioUsuario:

    def __init__(self, session: Session):
        
        self.session = session

    def criar(self, usuario: schemas.Usuario):
        
        usuario_bd = models.Usuario(
            nome=usuario.nome,
            senha=usuario.senha,
            telefone=usuario.telefone)
        
        self.session.add(usuario_bd)
        self.session.commit()
        self.session.refresh(usuario_bd)
        
        return usuario_bd


    def listar(self):
        
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).all()

        return usuarios

    def obter(self):
        pass

    def remover(self):
        pass    
