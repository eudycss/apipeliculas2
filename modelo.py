import numbers
from pydantic import BaseModel
from typing import Optional

class Peliculas(BaseModel):
    id: Optional[int]
    Nombre: str
    Fecha: str
    Comentario: str
