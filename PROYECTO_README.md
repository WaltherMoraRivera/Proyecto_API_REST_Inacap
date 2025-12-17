# Proyecto API REST - Sistema de Gestión de Festival de Cine
**INACAP 2025 - Programación de Objetos**

## 📋 Descripción del Proyecto

Sistema completo de gestión de festival de cine que integra:
- **Base de Datos Oracle** con tablas, triggers, stored procedures y transacciones
- **API REST** con FastAPI y autenticación JWT
- **Interfaz Gráfica** con PyQt6 para gestión visual

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                     USUARIO FINAL                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
┌───────▼────────┐           ┌────────▼────────┐
│  PyQt6 Client  │    HTTP   │   FastAPI       │
│  (Desktop UI)  │◄─────────►│   REST API      │
│  Login + CRUD  │   JWT     │  Port 8000      │
└────────────────┘           └────────┬────────┘
                                      │
                             ┌────────▼────────┐
                             │ Oracle Database │
                             │ Triggers + SP   │
                             └─────────────────┘
```

## 🚀 Características Implementadas

### ✅ Base de Datos Oracle
- **Tablas**: 11 tablas con PK/FK y constraints
- **Bitácoras**: 5 tablas de auditoría
- **Triggers**: Auditoría automática de cambios (INSERT, UPDATE, DELETE)
- **Stored Procedures**: CRUD completo + autenticación
- **Transacciones**: COMMIT/ROLLBACK en operaciones complejas

### ✅ API REST (FastAPI)
- **Endpoints**: `/peliculas` (CRUD completo)
- **Autenticación**: `/auth/login`, `/auth/register`, `/auth/logout`
- **Tokens JWT**: Autenticación basada en tokens
- **Validación**: Pydantic schemas
- **Documentación**: Swagger UI en `/docs`

### ✅ Cliente PyQt6
- **Login**: Interfaz de autenticación
- **CRUD Visual**: Tabla interactiva de películas
- **Formularios**: Crear y editar películas
- **Permisos**: Restricciones por rol de usuario

## 📁 Estructura del Proyecto

```
Proyecto_API_Rest_Inacap/
│
├── webApiRestFul/                  # Backend FastAPI
│   ├── app/
│   │   ├── domain/models/          # Entidades de dominio
│   │   ├── infrastructure/         # Repositorios y BD
│   │   └── api/                    # Controllers, Services, Schemas
│   ├── config/                     # Configuración
│   ├── sql/                        # Scripts SQL
│   ├── main.py                     # Punto de entrada
│   └── requirements.txt
│
├── pyqt6/                          # Frontend Desktop
│   ├── app/
│   │   ├── domain/models/          # Entidades
│   │   ├── infrastructure/         # Repositorios HTTP
│   │   ├── viewmodels/             # Lógica de presentación
│   │   └── ui/                     # Interfaces gráficas
│   ├── config/                     # Configuración
│   ├── main.py                     # Punto de entrada
│   └── requirements.txt
│
├── Base_de_Datos.sql              # Script original de BD
└── README.md                       # Este archivo
```

## ⚙️ Instalación y Configuración

### Requisitos Previos
- Python 3.10 o superior
- Oracle Database 19c o superior
- Oracle Instant Client (opcional, para thick mode)

### 1. Configurar Base de Datos

```bash
# Ejecutar scripts SQL en orden:
sqlplus usuario/password@servicio @webApiRestFul/sql/01_create_tables.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/02_create_audit_tables.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/03_create_triggers.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/04_create_stored_procedures_crud.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/05_create_stored_procedures_auth.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/06_create_stored_procedures_transactions.sql
sqlplus usuario/password@servicio @webApiRestFul/sql/07_insert_sample_data.sql
```

### 2. Configurar API (Backend)

```bash
cd webApiRestFul

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows

# Instalar dependencias
pip install -r requirements.txt

# Configurar settings.json
cp config/settings.example.json config/settings.json
# Editar config/settings.json con credenciales de Oracle
```

**Editar `config/settings.json`**:
```json
{
  "oracle": {
    "user": "TU_USUARIO",
    "password": "TU_PASSWORD",
    "dsn": "TU_DSN",
    "wallet_dir": null
  }
}
```

### 3. Configurar Cliente PyQt6

```bash
cd pyqt6

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 🎯 Ejecución

### 1. Iniciar la API

```bash
cd webApiRestFul
venv\Scripts\activate
python main.py
```

La API estará disponible en:
- **API**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs

### 2. Iniciar Cliente PyQt6

```bash
cd pyqt6
venv\Scripts\activate
python main.py
```

**Credenciales de prueba**:
- Usuario: `admin`
- Contraseña: `admin123`

## 🔐 Autenticación

El sistema utiliza **JWT (JSON Web Tokens)** para autenticación:

1. El usuario ingresa credenciales en PyQt6
2. PyQt6 envía POST a `/auth/login`
3. API valida con stored procedure `sp_login`
4. Si es válido, retorna token JWT
5. PyQt6 incluye token en todas las peticiones subsiguientes

## 📊 Endpoints de la API

### Autenticación
- `POST /auth/login` - Iniciar sesión
- `POST /auth/register` - Registrar usuario
- `POST /auth/logout` - Cerrar sesión
- `POST /auth/change-password` - Cambiar contraseña
- `GET /auth/verify` - Verificar token

### Películas (requiere autenticación)
- `GET /peliculas/` - Listar todas
- `GET /peliculas/{id}` - Obtener por ID
- `POST /peliculas/` - Crear nueva
- `PUT /peliculas/{id}` - Actualizar
- `DELETE /peliculas/{id}` - Eliminar (solo admin)

## 🗄️ Stored Procedures Principales

### CRUD
- `sp_crear_pelicula`
- `sp_leer_pelicula`
- `sp_listar_peliculas`
- `sp_actualizar_pelicula`
- `sp_eliminar_pelicula`

### Autenticación
- `sp_login` - Valida credenciales y registra acceso
- `sp_logout` - Registra cierre de sesión
- `sp_crear_usuario` - Crea nuevo usuario
- `sp_cambiar_password` - Cambia contraseña

### Transacciones
- `sp_registrar_asistencia_completa` - Registra asistente y asistencia
- `sp_programar_funcion_pelicula` - Crea función con proyección
- `sp_cancelar_funcion_reembolso` - Cancela función y elimina asistencias

## 🔍 Triggers de Auditoría

Todos los triggers registran automáticamente:
- Usuario que realizó la operación
- Fecha y hora
- Valores anteriores y nuevos
- Tipo de operación (INSERT/UPDATE/DELETE)

Tablas auditadas:
- `pelicula` → `bitacora_pelicula`
- `funcion` → `bitacora_funcion`
- `asistencia` → `bitacora_asistencia`
- `evaluacion` → `bitacora_evaluacion`
- `usuario` → `bitacora_usuario`

## 🎨 Patrones de Diseño Utilizados

- **Repository Pattern**: Abstracción de acceso a datos
- **MVVM**: Separación de lógica de presentación (PyQt6)
- **Dependency Injection**: Inversión de dependencias
- **DTO (Data Transfer Objects)**: Pydantic schemas
- **Factory Pattern**: Creación de conexiones
- **Layered Architecture**: Dominio, Infraestructura, Aplicación, Presentación

## 📚 Tecnologías Utilizadas

### Backend
- **FastAPI** 0.110.0 - Framework web
- **Uvicorn** - Servidor ASGI
- **oracledb** 2.0.1 - Driver de Oracle
- **PyJWT** - Autenticación JWT
- **Pydantic** - Validación de datos

### Frontend
- **PyQt6** 6.6.0 - Framework GUI
- **requests** - Cliente HTTP

### Base de Datos
- **Oracle Database** 19c o superior
- **PL/SQL** - Stored procedures y triggers

## 🧪 Pruebas

### Probar API con Swagger
1. Ir a http://localhost:8000/docs
2. Probar endpoint `/auth/login`
3. Copiar el token
4. Click en "Authorize" y pegar el token
5. Probar endpoints de películas

### Probar con PyQt6
1. Ejecutar `main.py`
2. Login con `admin` / `admin123`
3. Crear, editar y eliminar películas
4. Observar validaciones y mensajes

## 🔧 Troubleshooting

### Error de conexión a Oracle
- Verificar credenciales en `config/settings.json`
- Verificar que Oracle esté ejecutándose
- Si usa Autonomous DB, verificar Wallet

### Error 401 en API
- Token expirado (válido por 60 minutos)
- Cerrar sesión y volver a iniciar

### PyQt6 no se conecta a la API
- Verificar que la API esté ejecutándose
- Verificar URL en `pyqt6/config/settings.json`

## 👥 Autor

**Walther Mora Rivera**  
INACAP 2025 - Programación de Objetos

## 📄 Licencia

Proyecto académico - INACAP 2025
