"""
Servicio de negocio para Películas
"""
from typing import List, Optional
from app.domain.models.pelicula import Pelicula
from app.infrastructure.repositories.pelicula_repository import PeliculaRepository


class PeliculaService:
    """Servicio para lógica de negocio de Películas"""
    
    def __init__(self, repository: PeliculaRepository):
        """
        Inicializa el servicio
        
        Args:
            repository: Instancia de PeliculaRepository
        """
        self._repository = repository
    
    def get_all(self) -> List[Pelicula]:
        """Obtiene todas las películas"""
        return self._repository.get_all()
    
    def get_by_id(self, pelicula_id: int) -> Optional[Pelicula]:
        """Obtiene una película por ID"""
        return self._repository.get_by_id(pelicula_id)
    
    def create(self, pelicula: Pelicula) -> int:
        """Crea una nueva película"""
        # Aquí se pueden agregar validaciones de negocio adicionales
        return self._repository.create(pelicula)
    
    def update(self, pelicula_id: int, pelicula: Pelicula) -> None:
        """Actualiza una película existente"""
        # Verificar que existe
        existing = self._repository.get_by_id(pelicula_id)
        if not existing:
            raise ValueError(f"Película con ID {pelicula_id} no encontrada")
        
        pelicula.id_pelicula = pelicula_id
        self._repository.update(pelicula)
    
    def delete(self, pelicula_id: int) -> None:
        """Elimina una película"""
        self._repository.delete(pelicula_id)
