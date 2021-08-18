from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():

    return {'mensagem':'Olá cambada de lá ela!'}


@app.get('/profile')
def profile():

    return {'profile':'Ramon R. Valeriano'}


@app.post('/profile')
def signup():

    return {'mensagem':'Perfil Enviado com Sucesso!'}


@app.put('/profile')
def atualizar():

    return {'mensagem':'Perfil Atualizado com Sucesso!'}


@app.delete('/profile')
def deletar():

    return {'mensage':'Perfil Deletado com Sucesso!'}