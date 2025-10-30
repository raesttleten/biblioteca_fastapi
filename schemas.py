from pydantic import BaseModel, Field, validator
from typing import List, Optional

class AutorCreate(BaseModel):
    nombre: str = Field(..., min_length=2)
    pais_origen: str
    anio_nacimiento: int

class LibroCreate(BaseModel):
    titulo: str
    isbn: str = Field(..., min_length=10, max_length=13)
    anio_publicacion: int
    copias_disponibles: int = Field(..., ge=0)
    autores_ids: List[int]

    @validator('anio_publicacion')
    def validar_anio(cls, v):
        if v < 1400 or v > 2025:
            raise ValueError("Año de publicación no válido.")
        return v
