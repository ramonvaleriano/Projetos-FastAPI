from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():

    return {'mensagem':'Olá cambada de lá ela!'}