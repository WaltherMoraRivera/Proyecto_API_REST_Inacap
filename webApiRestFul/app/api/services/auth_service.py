"""
Servicio de autenticación y gestión de usuarios
"""
from typing import Tuple, Optional
from datetime import datetime, timedelta
from app.domain.models.usuario import Usuario
from app.infrastructure.repositories.usuario_repository import UsuarioRepository
import jwt


class AuthService:
    """Servicio para autenticación y manejo de tokens JWT"""
    
    # Configuración JWT (en producción mover a variables de entorno)
    SECRET_KEY = "tu_clave_secreta_super_segura_cambiar_en_produccion"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    
    def __init__(self, repository: UsuarioRepository):
        """
        Inicializa el servicio
        
        Args:
            repository: Instancia de UsuarioRepository
        """
        self._repository = repository
    
    def login(self, username: str, password: str) -> Tuple[bool, Optional[dict], str, Optional[str]]:
        """
        Realiza el login y genera token JWT
        
        Args:
            username: Nombre de usuario
            password: Contraseña
            
        Returns:
            Tupla (éxito, datos_usuario, mensaje, token)
        """
        success, usuario, mensaje = self._repository.login(username, password)
        
        if success and usuario:
            # Generar token JWT
            token = self._create_access_token(
                data={"sub": usuario.username, "rol": usuario.rol, "id": usuario.id_usuario}
            )
            
            usuario_dict = {
                "id_usuario": usuario.id_usuario,
                "username": usuario.username,
                "nombre_completo": usuario.nombre_completo,
                "email": usuario.email,
                "rol": usuario.rol
            }
            
            return True, usuario_dict, mensaje, token
        else:
            return False, None, mensaje, None
    
    def logout(self, id_usuario: int, username: str) -> None:
        """Registra el logout"""
        self._repository.logout(id_usuario, username)
    
    def create_usuario(self, usuario: Usuario, password: str) -> int:
        """Crea un nuevo usuario"""
        return self._repository.create_usuario(usuario, password)
    
    def cambiar_password(
        self, 
        id_usuario: int, 
        password_actual: str, 
        password_nuevo: str
    ) -> Tuple[bool, str]:
        """Cambia la contraseña de un usuario"""
        return self._repository.cambiar_password(id_usuario, password_actual, password_nuevo)
    
    def _create_access_token(self, data: dict) -> str:
        """
        Crea un token JWT
        
        Args:
            data: Datos a incluir en el token
            
        Returns:
            Token JWT
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Optional[dict]:
        """
        Verifica y decodifica un token JWT
        
        Args:
            token: Token JWT
            
        Returns:
            Payload del token o None si es inválido
        """
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.JWTError:
            return None
