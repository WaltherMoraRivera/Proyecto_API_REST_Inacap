# Backend FastAPI - Sistema de Gestión de Festival de Cine

API REST construida con FastAPI que proporciona endpoints para gestión de películas, funciones, asistentes y más, con autenticación JWT.

## Características

- ✅ Autenticación JWT
- ✅ CRUD completo de películas
- ✅ Conexión a Oracle Database
- ✅ Stored Procedures para lógica de negocio
- ✅ Documentación automática con Swagger
- ✅ Validación de datos con Pydantic
- ✅ Arquitectura en capas

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos
cp config/settings.example.json config/settings.json
# Editar config/settings.json con credenciales de Oracle
```

## Ejecución

```bash
python main.py
```

La API estará disponible en:
- API: http://localhost:8000
- Documentación: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Autenticación
- `POST /auth/login` - Iniciar sesión
- `POST /auth/register` - Registrar usuario
- `POST /auth/logout` - Cerrar sesión

### Películas
- `GET /peliculas/` - Listar todas
- `GET /peliculas/{id}` - Obtener por ID
- `POST /peliculas/` - Crear nueva
- `PUT /peliculas/{id}` - Actualizar
- `DELETE /peliculas/{id}` - Eliminar

## Estructura

```
webApiRestFul/
├── app/
│   ├── domain/models/          # Entidades de dominio
│   ├── infrastructure/         # Repositorios y BD
│   │   ├── database/           # Conexión Oracle
│   │   └── repositories/       # Acceso a datos
│   └── api/                    # API Layer
│       ├── controllers/        # Endpoints
│       ├── services/           # Lógica de negocio
│       └── schemas/            # Validación Pydantic
├── config/                     # Configuración
├── sql/                        # Scripts de BD
└── main.py                     # Punto de entrada
```

## Configuración

Editar `config/settings.json`:

```json
{
  "oracle": {
    "user": "ADMIN",
    "password": "password",
    "dsn": "servicio_high"
  }
}
```
