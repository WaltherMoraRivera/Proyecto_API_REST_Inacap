"""
ViewModel para gestión de Películas
"""
from PyQt6.QtCore import QObject, pyqtSignal
from typing import List, Optional
from app.domain.models.pelicula import Pelicula
from app.infrastructure.repositories.pelicula_repository import PeliculaRepository


class PeliculaViewModel(QObject):
    """ViewModel para lógica de presentación de Películas"""
    
    # Signals para notificar cambios a la vista
    peliculas_changed = pyqtSignal(list)
    error_occurred = pyqtSignal(str)
    success_message = pyqtSignal(str)
    
    def __init__(self, repository: PeliculaRepository):
        """
        Inicializa el ViewModel
        
        Args:
            repository: Instancia de PeliculaRepository
        """
        super().__init__()
        self._repository = repository
        self._peliculas: List[Pelicula] = []
    
    def load_peliculas(self):
        """Carga todas las películas desde la API"""
        try:
            self._peliculas = self._repository.get_all()
            self.peliculas_changed.emit(self._peliculas)
        except Exception as e:
            self.error_occurred.emit(f"Error al cargar películas: {str(e)}")
    
    def create_pelicula(self, pelicula: Pelicula):
        """Crea una nueva película"""
        try:
            result = self._repository.create(pelicula)
            self.success_message.emit("Película creada correctamente")
            self.load_peliculas()  # Recargar lista
        except Exception as e:
            self.error_occurred.emit(f"Error al crear película: {str(e)}")
    
    def update_pelicula(self, pelicula: Pelicula):
        """Actualiza una película existente"""
        try:
            result = self._repository.update(pelicula)
            self.success_message.emit("Película actualizada correctamente")
            self.load_peliculas()  # Recargar lista
        except Exception as e:
            self.error_occurred.emit(f"Error al actualizar película: {str(e)}")
    
    def delete_pelicula(self, pelicula_id: int):
        """Elimina una película"""
        try:
            result = self._repository.delete(pelicula_id)
            self.success_message.emit("Película eliminada correctamente")
            self.load_peliculas()  # Recargar lista
        except Exception as e:
            self.error_occurred.emit(f"Error al eliminar película: {str(e)}")
    
    @property
    def peliculas(self) -> List[Pelicula]:
        """Retorna la lista de películas"""
        return self._peliculas
