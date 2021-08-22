import requests

retorno = requests.get('http://localhost:8000/root')

print(f'{retorno.json()}')