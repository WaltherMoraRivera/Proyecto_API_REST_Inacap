"""
Modelo de dominio: Usuario
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Usuario:
    """Entidad de dominio para Usuario"""
    id_usuario: Optional[int]
    username: str
    password_hash: str
    nombre_completo: str
    email: str
    rol: str
    activo: bool
    fecha_creacion: Optional[datetime] = None
    ultimo_acceso: Optional[datetime] = None
