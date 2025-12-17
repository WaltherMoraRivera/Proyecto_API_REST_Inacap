"""
Repositorio para gestión de Películas
"""
from typing import List, Optional
import oracledb
from app.domain.models.pelicula import Pelicula
from app.infrastructure.database.oracle_connection import OracleConnection


class PeliculaRepository:
    """Repositorio para operaciones CRUD de Película"""
    
    def __init__(self, connection: OracleConnection):
        """
        Inicializa el repositorio
        
        Args:
            connection: Instancia de OracleConnection
        """
        self._connection = connection
    
    def get_all(self) -> List[Pelicula]:
        """Obtiene todas las películas"""
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.callproc("sp_listar_peliculas", [cursor])
            
            peliculas = []
            for row in cursor.getvalue(0):
                peliculas.append(Pelicula(*row))
            
            return peliculas
    
    def get_by_id(self, pelicula_id: int) -> Optional[Pelicula]:
        """
        Obtiene una película por ID
        
        Args:
            pelicula_id: ID de la película
            
        Returns:
            Película o None si no existe
        """
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            ref_cursor = conn.cursor()
            
            cursor.callproc("sp_leer_pelicula", [pelicula_id, ref_cursor])
            
            row = ref_cursor.fetchone()
            if row:
                return Pelicula(*row)
            return None
    
    def create(self, pelicula: Pelicula) -> int:
        """
        Crea una nueva película
        
        Args:
            pelicula: Instancia de Pelicula
            
        Returns:
            ID de la película creada
        """
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            id_pelicula = cursor.var(oracledb.NUMBER)
            
            cursor.callproc("sp_crear_pelicula", [
                pelicula.titulo,
                pelicula.pais_origen,
                pelicula.director,
                pelicula.duracion_minutos,
                pelicula.genero,
                pelicula.clasificacion,
                pelicula.sinopsis,
                id_pelicula
            ])
            
            return int(id_pelicula.getvalue())
    
    def update(self, pelicula: Pelicula) -> None:
        """
        Actualiza una película existente
        
        Args:
            pelicula: Instancia de Pelicula con datos actualizados
        """
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.callproc("sp_actualizar_pelicula", [
                pelicula.id_pelicula,
                pelicula.titulo,
                pelicula.pais_origen,
                pelicula.director,
                pelicula.duracion_minutos,
                pelicula.genero,
                pelicula.clasificacion,
                pelicula.sinopsis
            ])
    
    def delete(self, pelicula_id: int) -> None:
        """
        Elimina una película
        
        Args:
            pelicula_id: ID de la película a eliminar
        """
        with self._connection.get_connection() as conn:
            cursor = conn.cursor()
            cursor.callproc("sp_eliminar_pelicula", [pelicula_id])
