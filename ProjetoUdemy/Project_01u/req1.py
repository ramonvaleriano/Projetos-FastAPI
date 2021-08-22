import requests

retorno = requests.post('http://localhost:8000/usuario/', params={"nome":"joao"})

print(retorno.json())