import requests

retorno = requests.post("http://127.0.0.1:8000/usuarios/", params={'nome': 'alefe'})
print(retorno.json())