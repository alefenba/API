from fastapi import FastAPI

app = FastAPI()

usuarios = [(1, 'caio', 'minhasenha1'), (2, 'joao', 'minhasenha2'), (3, 'alefe', 'minhasenha3')]


@app.post('/usuarios')
def main (nome):
    for i in usuarios :
        if i[1] == nome:
            return i[1:3]

    return "Usuario não encontrado"