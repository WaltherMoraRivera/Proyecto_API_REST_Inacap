"""
Controlador para endpoints de Autenticación
"""
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional
from app.api.schemas.auth_schema import (
    LoginSchema, 
    LoginResponseSchema,
    UsuarioCreateSchema,
    CambiarPasswordSchema
)
from app.api.services.auth_service import AuthService
from app.infrastructure.repositories.usuario_repository import UsuarioRepository
from app.infrastructure.database.oracle_connection import OracleConnection
from app.domain.models.usuario import Usuario
from pathlib import Path


router = APIRouter(prefix="/auth", tags=["Autenticación"])


def get_auth_service() -> AuthService:
    """Dependency para obtener el servicio de autenticación"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "settings.json"
    connection = OracleConnection.from_settings_file(config_path)
    repository = UsuarioRepository(connection)
    return AuthService(repository)


def verify_token_dependency(
    authorization: Optional[str] = Header(None),
    auth_service: AuthService = Depends(get_auth_service)
) -> dict:
    """Dependency para verificar token JWT"""
    if not authorization:
        raise HTTPException(status_code=401, detail="Token no proporcionado")
    
    try:
        # Extraer token del header "Bearer <token>"
        scheme, token = authorization.split()
        if scheme.lower() != 'bearer':
            raise HTTPException(status_code=401, detail="Esquema de autenticación inválido")
    except ValueError:
        raise HTTPException(status_code=401, detail="Header de autorización inválido")
    
    payload = auth_service.verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    return payload


@router.post("/login", response_model=LoginResponseSchema)
def login(credentials: LoginSchema, auth_service: AuthService = Depends(get_auth_service)):
    """
    Endpoint de login
    
    Verifica credenciales y retorna un token JWT
    """
    success, usuario, mensaje, token = auth_service.login(
        credentials.username, 
        credentials.password
    )
    
    if not success:
        raise HTTPException(status_code=401, detail=mensaje)
    
    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": usuario
    }


@router.post("/register", status_code=201)
def register(
    user_data: UsuarioCreateSchema,
    auth_service: AuthService = Depends(get_auth_service)
):
    """
    Endpoint para registrar un nuevo usuario
    """
    try:
        usuario = Usuario(
            id_usuario=None,
            username=user_data.username,
            password_hash="",  # Se manejará en el repositorio
            nombre_completo=user_data.nombre_completo,
            email=user_data.email,
            rol=user_data.rol,
            activo=True
        )
        
        id_usuario = auth_service.create_usuario(usuario, user_data.password)
        
        return {
            "message": "Usuario creado correctamente",
            "id_usuario": id_usuario
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/logout")
def logout(
    current_user: dict = Depends(verify_token_dependency),
    auth_service: AuthService = Depends(get_auth_service)
):
    """
    Endpoint de logout
    
    Registra el cierre de sesión del usuario
    """
    auth_service.logout(current_user["id"], current_user["sub"])
    
    return {"message": "Logout exitoso"}


@router.post("/change-password")
def change_password(
    password_data: CambiarPasswordSchema,
    current_user: dict = Depends(verify_token_dependency),
    auth_service: AuthService = Depends(get_auth_service)
):
    """
    Endpoint para cambiar contraseña
    """
    success, mensaje = auth_service.cambiar_password(
        current_user["id"],
        password_data.password_actual,
        password_data.password_nuevo
    )
    
    if not success:
        raise HTTPException(status_code=400, detail=mensaje)
    
    return {"message": mensaje}


@router.get("/verify")
def verify_token(current_user: dict = Depends(verify_token_dependency)):
    """
    Endpoint para verificar si un token es válido
    """
    return {
        "valid": True,
        "user": current_user["sub"],
        "rol": current_user["rol"]
    }
