from fastapi import FastAPI, status

app = FastAPI()

@app.get('/', status_code=status.HTTP_200_OK)
def home():

    return {'mensagem':'Testando Aplicação!'}