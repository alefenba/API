from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str


@app.post('/usuario')
def main (usuario:Usuario):
    return usuario