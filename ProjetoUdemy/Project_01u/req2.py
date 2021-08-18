import requests

usuario = {
    "id" : 0,
    "nome" : "Ramon Valeriano",
    "senha" : "123465"
}

retorno = requests.post('http://localhost:8000/usuario', params={
    'id':34, 'nome':'um chato', 'senha':'umaqualquer'})

print(retorno.json())