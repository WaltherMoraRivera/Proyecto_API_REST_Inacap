"""
Aplicación principal FastAPI - Sistema de Gestión de Festival de Cine
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.controllers import auth_controller, pelicula_controller


# Crear instancia de FastAPI
app = FastAPI(
    title="API Festival de Cine",
    description="API REST para gestión de festival de cine con autenticación JWT",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para permitir peticiones desde PyQt6
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(auth_controller.router)
app.include_router(pelicula_controller.router)


@app.get("/")
def root():
    """Endpoint raíz"""
    return {
        "message": "API Festival de Cine - INACAP 2025",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """Endpoint de salud"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
