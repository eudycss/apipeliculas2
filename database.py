from fastapi import FastAPI, HTTPException
from peewee import *
from modelo import *
from uuid import uuid4 as uuid

db = SqliteDatabase('Peli.db')

class t_Peliculas(Model):
    Nombre = TextField()
    Fecha = TextField()
    Comentario = TextField()

    class Meta:
        database = db

db.connect()
db.create_tables([t_Peliculas])

#Función para guardar peliculas

def GuardarPeliculas(p:Peliculas):
    tp = t_Peliculas()
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.save()
    
def CargarPeliculas():
    tp = []

    for p in t_Peliculas.select().dicts():
        tp.append(p)
    return tp 

# By id
def CargarPelById(post_id: str):
    for post in t_Peliculas.select().dicts():
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")

def ActualizarPeliculas(p:Peliculas):
    tp = t_Peliculas().get(t_Peliculas.id == p.id)
    tp.Nombre = p.Nombre
    tp.Fecha = p.Fecha
    tp.Comentario = p.Comentario
    tp.save()

def EliminarPeliculas(post_id: str):
    tp = t_Peliculas().get(t_Peliculas.id == post_id)
    tp.delete_instance(post_id)
    tp.save()

# def EliminarPeliculas(p:Peliculas):
#     tp = t_Peliculas().get(t_Peliculas.id == p.id)
#     tp.delete_instance(p.id)
#     tp.save()