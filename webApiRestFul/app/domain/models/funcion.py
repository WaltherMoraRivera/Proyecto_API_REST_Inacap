"""
Modelo de dominio: Función
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Funcion:
    """Entidad de dominio para Función"""
    id_funcion: Optional[int]
    fecha: datetime
    hora: str
    precio_entrada: float
    estado_funcion: str
    observaciones: str
    id_sede: int
