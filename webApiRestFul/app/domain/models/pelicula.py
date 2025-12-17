"""
Modelo de dominio: Película
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Pelicula:
    """Entidad de dominio para Película"""
    id_pelicula: Optional[int]
    titulo: str
    pais_origen: str
    director: str
    duracion_minutos: int
    genero: str
    clasificacion: str
    sinopsis: str
