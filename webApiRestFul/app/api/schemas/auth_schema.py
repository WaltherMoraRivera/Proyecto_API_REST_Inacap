"""
Schemas Pydantic para Autenticación y Usuario
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class LoginSchema(BaseModel):
    """Schema para login"""
    username: str = Field(..., min_length=3, max_length=50, description="Nombre de usuario")
    password: str = Field(..., min_length=6, description="Contraseña")


class LoginResponseSchema(BaseModel):
    """Schema para respuesta de login"""
    access_token: str
    token_type: str = "bearer"
    usuario: dict


class UsuarioCreateSchema(BaseModel):
    """Schema para crear usuario"""
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)
    nombre_completo: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    rol: str = Field(default="usuario", description="Rol del usuario")


class UsuarioResponseSchema(BaseModel):
    """Schema para respuesta de usuario"""
    id_usuario: Optional[int]
    username: str
    nombre_completo: str
    email: str
    rol: str
    activo: bool
    fecha_creacion: Optional[datetime] = None
    ultimo_acceso: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class CambiarPasswordSchema(BaseModel):
    """Schema para cambiar contraseña"""
    password_actual: str = Field(..., min_length=6)
    password_nuevo: str = Field(..., min_length=6)
