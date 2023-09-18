from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Documentación API1 TIVAPP"
app.version = "0.0.1"


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: str


@app.get("/")
def index():
    return {'message': 'hola mundo'}


@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}


@app.post("/libros")
def insertar_libro(libro: Libro):
    return {"message": f"libro {libro.titulo} insertado"}
