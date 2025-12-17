"""
Repositorio HTTP para gestión de Películas (Cliente API)
"""
from typing import List, Optional
import requests
from app.domain.models.pelicula import Pelicula


class PeliculaRepository:
    """Repositorio que consume la API REST para Películas"""
    
    def __init__(self, api_base_url: str, token: str):
        """
        Inicializa el repositorio
        
        Args:
            api_base_url: URL base de la API
            token: Token JWT para autenticación
        """
        self._base_url = f"{api_base_url}/peliculas"
        self._headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
    
    def get_all(self) -> List[Pelicula]:
        """Obtiene todas las películas"""
        response = requests.get(self._base_url, headers=self._headers)
        response.raise_for_status()
        
        peliculas = []
        for item in response.json():
            peliculas.append(Pelicula(**item))
        
        return peliculas
    
    def get_by_id(self, pelicula_id: int) -> Optional[Pelicula]:
        """Obtiene una película por ID"""
        response = requests.get(f"{self._base_url}/{pelicula_id}", headers=self._headers)
        response.raise_for_status()
        
        data = response.json()
        return Pelicula(**data)
    
    def create(self, pelicula: Pelicula) -> dict:
        """Crea una nueva película"""
        data = {
            "titulo": pelicula.titulo,
            "pais_origen": pelicula.pais_origen,
            "director": pelicula.director,
            "duracion_minutos": pelicula.duracion_minutos,
            "genero": pelicula.genero,
            "clasificacion": pelicula.clasificacion,
            "sinopsis": pelicula.sinopsis
        }
        
        response = requests.post(self._base_url, json=data, headers=self._headers)
        response.raise_for_status()
        
        return response.json()
    
    def update(self, pelicula: Pelicula) -> dict:
        """Actualiza una película existente"""
        data = {
            "titulo": pelicula.titulo,
            "pais_origen": pelicula.pais_origen,
            "director": pelicula.director,
            "duracion_minutos": pelicula.duracion_minutos,
            "genero": pelicula.genero,
            "clasificacion": pelicula.clasificacion,
            "sinopsis": pelicula.sinopsis
        }
        
        response = requests.put(
            f"{self._base_url}/{pelicula.id_pelicula}",
            json=data,
            headers=self._headers
        )
        response.raise_for_status()
        
        return response.json()
    
    def delete(self, pelicula_id: int) -> dict:
        """Elimina una película"""
        response = requests.delete(
            f"{self._base_url}/{pelicula_id}",
            headers=self._headers
        )
        response.raise_for_status()
        
        return response.json()
