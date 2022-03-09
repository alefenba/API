from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str

lista = [
    Usuario(id=1,nome='caio',senha="minhasenha1"),
    Usuario(id=2,nome='joao',senha="minhasenha2"),
    Usuario(id=3,nome='Alefe',senha="minhasenha3")
]

@app.post('/usuario')
def main (usuario:Usuario):
    lista.append(usuario)
    return "Usuario cadastrado"


@app.get('/usuariolistar')
def main():
    return lista