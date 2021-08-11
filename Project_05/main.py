from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():

    return {'msg':'Bem vindo a nossa aplicação.'}