# Importando a classe base que será o modelo de analise
# de saída dos dados.
from pydantic import BaseModel

# Lib responsável por deixar como opcional o tipo de uma variável
# Lib responsável por tipa uma lista para a model
from typing import Optional, List


class Usuario(BaseModel):
    """
        Model que caracteriza o usuário
    """
    
    id : Optional[str] =  None
    nome : str
    telefone : str
    #meus_produto : List[Produto]
    #minhas_vendas : List[Pedido]
    #meus_pedidos : List[Pedido]


class Produto(BaseModel):
    """
        Model que caracteriza o produto
    """

    id : Optional[str] = None
    #usuario : Usuario
    nome : str
    detalhes : str
    preco : float
    disponivel : bool = False

    class Config:

        orm_mode = True


class ProdutoSimples(BaseModel):
    """
        Model que caracteriza a saída do produto
    """

    id : Optional[str] = None
    nome : str
    preco : float

    class Config:

        orm_mode = True


class Pedido(BaseModel):
    """
        Model que caracteriza o pedido
    """

    id : Optional[str] = None
    usuario : Usuario
    profuto : Produto
    quantidade : int
    entrega : bool = True
    endereco : str
    observacoes : Optional[str] = 'Sem Obsercações'