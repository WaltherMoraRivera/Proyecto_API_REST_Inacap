"""
Repositorio para gestión de Usuarios y Autenticación
"""
from typing import Optional, Tuple
import oracledb
import hashlib
from app.domain.models.usuario import Usuario
from app.infrastructure.database.oracle_connection import OracleConnection


class UsuarioRepository:
    """Repositorio para operaciones de Usuario y Autenticación"""
    
    def __init__(self, connection: OracleConnection):
        """
        Inicializa el repositorio
        
        Args:
            connection: Instancia de OracleConnection
        """
        self._connection = connection
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Genera hash SHA-256 de una contraseña
        
        Args:
            password: Contraseña en texto plano
            
        Returns:
            Hash SHA-256 de la contraseña
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_usuario(self, usuario: Usuario, password: str) -> int:
        """
        Crea un nuevo usuario
        
        Args:
            usuario: Instancia de Usuario
            password: Contraseña en texto plano
            
        Returns:
            ID del usuario creado
        """
        password_hash = self.hash_password(password)
        
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            id_usuario = cursor.var(oracledb.NUMBER)
            
            cursor.callproc("sp_crear_usuario", [
                usuario.username,
                password_hash,
                usuario.nombre_completo,
                usuario.email,
                usuario.rol,
                id_usuario
            ])
            
            return int(id_usuario.getvalue())
    
    def login(self, username: str, password: str) -> Tuple[bool, Optional[Usuario], str]:
        """
        Verifica credenciales de usuario
        
        Args:
            username: Nombre de usuario
            password: Contraseña en texto plano
            
        Returns:
            Tupla (éxito, usuario, mensaje)
        """
        password_hash = self.hash_password(password)
        
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            
            # Variables de salida
            id_usuario = cursor.var(oracledb.NUMBER)
            nombre_completo = cursor.var(oracledb.STRING)
            email = cursor.var(oracledb.STRING)
            rol = cursor.var(oracledb.STRING)
            resultado = cursor.var(oracledb.STRING)
            
            cursor.callproc("sp_login", [
                username,
                password_hash,
                id_usuario,
                nombre_completo,
                email,
                rol,
                resultado
            ])
            
            resultado_str = resultado.getvalue()
            
            if resultado_str == 'EXITOSO':
                usuario = Usuario(
                    id_usuario=int(id_usuario.getvalue()),
                    username=username,
                    password_hash=password_hash,
                    nombre_completo=nombre_completo.getvalue(),
                    email=email.getvalue(),
                    rol=rol.getvalue(),
                    activo=True
                )
                return True, usuario, "Login exitoso"
            elif resultado_str == 'USUARIO_INACTIVO':
                return False, None, "Usuario inactivo"
            elif resultado_str == 'PASSWORD_INCORRECTO':
                return False, None, "Contraseña incorrecta"
            elif resultado_str == 'USUARIO_NO_EXISTE':
                return False, None, "Usuario no existe"
            else:
                return False, None, "Error desconocido"
    
    def logout(self, id_usuario: int, username: str) -> None:
        """
        Registra el logout de un usuario
        
        Args:
            id_usuario: ID del usuario
            username: Nombre de usuario
        """
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.callproc("sp_logout", [id_usuario, username])
    
    def cambiar_password(
        self, 
        id_usuario: int, 
        password_actual: str, 
        password_nuevo: str
    ) -> Tuple[bool, str]:
        """
        Cambia la contraseña de un usuario
        
        Args:
            id_usuario: ID del usuario
            password_actual: Contraseña actual en texto plano
            password_nuevo: Nueva contraseña en texto plano
            
        Returns:
            Tupla (éxito, mensaje)
        """
        hash_actual = self.hash_password(password_actual)
        hash_nuevo = self.hash_password(password_nuevo)
        
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            resultado = cursor.var(oracledb.STRING)
            
            cursor.callproc("sp_cambiar_password", [
                id_usuario,
                hash_actual,
                hash_nuevo,
                resultado
            ])
            
            resultado_str = resultado.getvalue()
            
            if resultado_str == 'EXITOSO':
                return True, "Contraseña actualizada correctamente"
            elif resultado_str == 'PASSWORD_ACTUAL_INCORRECTO':
                return False, "Contraseña actual incorrecta"
            else:
                return False, resultado_str
