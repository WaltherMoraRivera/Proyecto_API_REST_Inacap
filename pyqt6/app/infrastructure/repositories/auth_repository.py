"""
Repositorio de autenticación HTTP
"""
import requests
from typing import Tuple, Optional


class AuthRepository:
    """Repositorio para autenticación con la API"""
    
    def __init__(self, api_base_url: str):
        """
        Inicializa el repositorio
        
        Args:
            api_base_url: URL base de la API
        """
        self._base_url = f"{api_base_url}/auth"
    
    def login(self, username: str, password: str) -> Tuple[bool, Optional[dict], Optional[str], Optional[str]]:
        """
        Realiza login en la API
        
        Args:
            username: Nombre de usuario
            password: Contraseña
            
        Returns:
            Tupla (éxito, datos_usuario, token, mensaje_error)
        """
        try:
            data = {
                "username": username,
                "password": password
            }
            
            response = requests.post(f"{self._base_url}/login", json=data)
            
            if response.status_code == 200:
                result = response.json()
                return True, result["usuario"], result["access_token"], None
            else:
                error_detail = response.json().get("detail", "Error desconocido")
                return False, None, None, error_detail
                
        except requests.RequestException as e:
            return False, None, None, f"Error de conexión: {str(e)}"
    
    def verify_token(self, token: str) -> bool:
        """
        Verifica si un token es válido
        
        Args:
            token: Token JWT
            
        Returns:
            True si el token es válido
        """
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(f"{self._base_url}/verify", headers=headers)
            return response.status_code == 200
        except:
            return False
