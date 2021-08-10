from fastapi import FastAPI

app = FastAPI()

@app.get('/saudacao/{nome}')
def saudacao(nome: str):

    mensagem = f'Olá {nome}"'

    return {'mensagem':mensagem}


@app.get('/calculo/{numero}')
def quadrado(numero: int):
    
    result = numero ** 2
    mensagem = f'O quadrado do número {numero} é {result}'

    return {'mensagem':mensagem}