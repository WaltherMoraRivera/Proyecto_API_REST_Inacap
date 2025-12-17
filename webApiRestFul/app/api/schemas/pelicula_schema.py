"""
Schemas Pydantic para Película
"""
from pydantic import BaseModel, Field
from typing import Optional


class PeliculaCreateSchema(BaseModel):
    """Schema para crear una película"""
    titulo: str = Field(..., min_length=1, max_length=100, description="Título de la película")
    pais_origen: str = Field(..., min_length=1, max_length=50, description="País de origen")
    director: str = Field(..., min_length=1, max_length=100, description="Director")
    duracion_minutos: int = Field(..., gt=0, description="Duración en minutos")
    genero: str = Field(default="Drama", max_length=50, description="Género")
    clasificacion: str = Field(default="TE", description="Clasificación")
    sinopsis: str = Field(default="Sin sinopsis disponible", max_length=500, description="Sinopsis")


class PeliculaUpdateSchema(BaseModel):
    """Schema para actualizar una película"""
    titulo: str = Field(..., min_length=1, max_length=100)
    pais_origen: str = Field(..., min_length=1, max_length=50)
    director: str = Field(..., min_length=1, max_length=100)
    duracion_minutos: int = Field(..., gt=0)
    genero: str = Field(..., max_length=50)
    clasificacion: str
    sinopsis: str = Field(..., max_length=500)


class PeliculaResponseSchema(BaseModel):
    """Schema para respuesta de película"""
    id_pelicula: Optional[int]
    titulo: str
    pais_origen: str
    director: str
    duracion_minutos: int
    genero: str
    clasificacion: str
    sinopsis: str
    
    class Config:
        from_attributes = True
