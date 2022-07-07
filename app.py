from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from modelo import *
import database as bd


app = FastAPI()

@app.get('/')
def read_root():
        return {"welcome": "Welcome to my API"}

@app.post("/Peliculas/Agregar", tags=['Peliculas'])
def Agregar (P:Peliculas):
    bd.GuardarPeliculas(P)
    return {"Mensaje":"Los datos fueron Guardados."}

@app.get("/Peliculas/Lista", tags=['Peliculas'])
def Lista_de_Peliculas():
    Peliculas = bd.CargarPeliculas()
    return Peliculas

@app.get("/Peliculas/Listabyid/{pe_id}", tags=['Peliculas'])
def Lista_PelyBy_id(pe_id:int):
    Peliculas = bd.CargarPelById(pe_id)
    return Peliculas

@app.put("/Peliculas/Actualizar",tags=['Peliculas'])
def Actualizar(P:Peliculas):
    bd.ActualizarPeliculas(P)
    return  {"Mensaje":"Los datos fueron actualizados."}


@app.delete("/Peliculas/Eliminar/{pe_id}",tags=['Peliculas'])
def Eliminar(pe_id:int):
    bd.EliminarPeliculas(pe_id)
    return  {"Mensaje":"La película fue eliminada."}

# @app.delete("/Peliculas/Eliminar/{pe_id}",tags=['Peliculas'])
# def Eliminar(P:Peliculas):
#     bd.EliminarPeliculas(P)
#     return  {"Mensaje":"La película fue eliminada."}
