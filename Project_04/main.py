from fastapi import FastAPI # Importando a classe que do fastAPI de fato
from pydantic import BaseModel # Importando a classe modelo, para dar corpo
                               # a requisição.

app = FastAPI()

@app.get('/')
def home():
    
    return {'mensagem':'Olá Mundo!'}

@app.get('/saudacao/{nome}')
def saudacao(nome: str):
    result = f'Seja bem vindo {nome}!'

    return {'mensage':result}


@app.get('/quadrado/{numero}')
def quadrado(numero: int):

    result = numero**2
    mensagem = f'O quadraro do número {numero} é {result}'

    return {'mensagem':mensagem}


@app.get('/dobro')
def dobro(valor: int):

    result = valor * 2
    mensagem = f'O dobro de {valor} é {result}'

    return {'mensagem':mensagem}


@app.get('/retangulo')
def area_retangulo(largura: int, altura: int = 2):

    area = largura * altura
    mensagem = f'A area do retangulo é {area}'

    return {'mensagem':mensagem} 
class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produto')
def produto(produto: Produto):

    mensagem = f'Produto {produto.nome} com preço R$ {produto.preco:.2f} foi cadastrado com Sucesso!'

    return {'mensagem':mensagem}