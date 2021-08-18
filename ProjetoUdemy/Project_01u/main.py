from fastapi import FastAPI

app = FastAPI()

@app.get('/root')
def root():

    return {'mensagem':'Olá mundo!'}


@app.get('/meunome/{nome_meu}')
def nome(nome_meu):

    mensagem = f'Seu nome é: {nome_meu}'

    return {'mensagem':mensagem}