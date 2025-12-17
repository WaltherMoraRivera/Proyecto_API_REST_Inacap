"""
Controlador para endpoints de Películas
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.api.schemas.pelicula_schema import (
    PeliculaCreateSchema,
    PeliculaUpdateSchema,
    PeliculaResponseSchema
)
from app.api.services.pelicula_service import PeliculaService
from app.infrastructure.repositories.pelicula_repository import PeliculaRepository
from app.infrastructure.database.oracle_connection import OracleConnection
from app.domain.models.pelicula import Pelicula
from app.api.controllers.auth_controller import verify_token_dependency
from pathlib import Path


router = APIRouter(prefix="/peliculas", tags=["Películas"])


def get_pelicula_service() -> PeliculaService:
    """Dependency para obtener el servicio de películas"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "settings.json"
    connection = OracleConnection.from_settings_file(config_path)
    repository = PeliculaRepository(connection)
    return PeliculaService(repository)


@router.get("/", response_model=List[PeliculaResponseSchema])
def get_all_peliculas(
    service: PeliculaService = Depends(get_pelicula_service),
    current_user: dict = Depends(verify_token_dependency)
):
    """
    Obtiene todas las películas
    
    Requiere autenticación
    """
    try:
        peliculas = service.get_all()
        return peliculas
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{pelicula_id}", response_model=PeliculaResponseSchema)
def get_pelicula(
    pelicula_id: int,
    service: PeliculaService = Depends(get_pelicula_service),
    current_user: dict = Depends(verify_token_dependency)
):
    """
    Obtiene una película por ID
    
    Requiere autenticación
    """
    try:
        pelicula = service.get_by_id(pelicula_id)
        if not pelicula:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        return pelicula
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", status_code=201)
def create_pelicula(
    pelicula_data: PeliculaCreateSchema,
    service: PeliculaService = Depends(get_pelicula_service),
    current_user: dict = Depends(verify_token_dependency)
):
    """
    Crea una nueva película
    
    Requiere autenticación
    """
    try:
        pelicula = Pelicula(
            id_pelicula=None,
            titulo=pelicula_data.titulo,
            pais_origen=pelicula_data.pais_origen,
            director=pelicula_data.director,
            duracion_minutos=pelicula_data.duracion_minutos,
            genero=pelicula_data.genero,
            clasificacion=pelicula_data.clasificacion,
            sinopsis=pelicula_data.sinopsis
        )
        
        id_pelicula = service.create(pelicula)
        
        return {
            "message": "Película creada correctamente",
            "id_pelicula": id_pelicula
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{pelicula_id}")
def update_pelicula(
    pelicula_id: int,
    pelicula_data: PeliculaUpdateSchema,
    service: PeliculaService = Depends(get_pelicula_service),
    current_user: dict = Depends(verify_token_dependency)
):
    """
    Actualiza una película existente
    
    Requiere autenticación
    """
    try:
        pelicula = Pelicula(
            id_pelicula=pelicula_id,
            titulo=pelicula_data.titulo,
            pais_origen=pelicula_data.pais_origen,
            director=pelicula_data.director,
            duracion_minutos=pelicula_data.duracion_minutos,
            genero=pelicula_data.genero,
            clasificacion=pelicula_data.clasificacion,
            sinopsis=pelicula_data.sinopsis
        )
        
        service.update(pelicula_id, pelicula)
        
        return {"message": "Película actualizada correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{pelicula_id}")
def delete_pelicula(
    pelicula_id: int,
    service: PeliculaService = Depends(get_pelicula_service),
    current_user: dict = Depends(verify_token_dependency)
):
    """
    Elimina una película
    
    Requiere autenticación y rol de administrador
    """
    # Verificar que el usuario sea administrador
    if current_user.get("rol") != "admin":
        raise HTTPException(status_code=403, detail="No tiene permisos para eliminar películas")
    
    try:
        service.delete(pelicula_id)
        return {"message": "Película eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
