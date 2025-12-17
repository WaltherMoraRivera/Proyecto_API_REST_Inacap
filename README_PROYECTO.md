# 🎬 Sistema de Gestión de Festival de Cine

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com/)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.6.0-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![Oracle](https://img.shields.io/badge/Oracle-19c+-red.svg)](https://www.oracle.com/database/)

> Sistema completo de gestión para un Festival de Cine con arquitectura cliente-servidor, autenticación JWT, y auditoría completa de operaciones.

[🚀 Inicio Rápido](#-inicio-rápido) • [📖 Documentación](#-documentación) • [🏗️ Arquitectura](#️-arquitectura) • [🔧 Instalación](#-instalación) • [🎯 Características](#-características)

---

## 🚀 Inicio Rápido

### Para Windows (Recomendado)

```batch
# 1. Iniciar API (Backend)
1_Iniciar_API.bat

# 2. Iniciar Cliente (en otra terminal)
2_Iniciar_Cliente.bat

# 3. Login
Usuario: admin
Password: admin123
```

### Manual

```powershell
# Terminal 1 - API
cd webApiRestFul
python main.py

# Terminal 2 - Cliente
cd pyqt6
python main.py
```

📖 **Guía completa**: [INICIO_RAPIDO.md](INICIO_RAPIDO.md)

---

## 📖 Documentación

| Documento | Descripción |
|-----------|-------------|
| [INICIO_RAPIDO.md](INICIO_RAPIDO.md) | Guía de inicio rápido con troubleshooting |
| [INSTRUCCIONES_BASE_DATOS.md](INSTRUCCIONES_BASE_DATOS.md) | Configuración de Oracle Database |
| [GUIA_EJECUCION.md](GUIA_EJECUCION.md) | Guía detallada de ejecución y pruebas |
| [CHANGELOG.md](CHANGELOG.md) | Historial de cambios y versiones |
| [API Swagger](http://localhost:8000/docs) | Documentación interactiva de la API |

---

## 🎯 Características

### ✅ Autenticación y Seguridad
- 🔐 Autenticación JWT (60 min de expiración)
- 🔒 Passwords hasheados con SHA-256
- 👥 Control de acceso basado en roles (admin/usuario)
- 📝 Auditoría completa en base de datos

### ✅ Gestión de Películas
- ➕ Crear nuevas películas
- ✏️ Editar información existente
- 🗑️ Eliminar películas (solo administradores)
- 🔍 Listar y buscar películas
- 📋 Campos: título, país, director, duración, género, clasificación, sinopsis

### ✅ Base de Datos Oracle
- 📊 16 tablas (11 principales + 5 auditoría)
- ⚡ 15+ stored procedures
- 🔔 15 triggers automáticos
- 📈 Bitácoras de auditoría completas

### ✅ Tecnologías
- 🌐 API REST con FastAPI
- 🖥️ Cliente de escritorio con PyQt6
- 🗄️ Oracle Autonomous Database
- 📚 Documentación Swagger automática

---

## 🏗️ Arquitectura

```
┌─────────────┐      HTTP/REST      ┌──────────────┐      SQL       ┌─────────────┐
│   PyQt6     │────────────────────►│   FastAPI    │───────────────►│   Oracle    │
│   Client    │◄────────────────────│     API      │◄───────────────│  Database   │
│  (Desktop)  │     JSON + JWT      │ (Port 8000)  │   Procedures   │  (Cloud/    │
└─────────────┘                     └──────────────┘                │  On-Prem)   │
                                                                     └─────────────┘
```

### Capas de la Arquitectura

#### 1. **Presentación**
- **PyQt6 UI**: Ventanas, formularios, tablas
- **FastAPI Controllers**: Endpoints HTTP

#### 2. **Aplicación**
- **ViewModels**: Lógica de presentación
- **Services**: Casos de uso y lógica de negocio

#### 3. **Dominio**
- **Models**: Entidades (Pelicula, Usuario, Funcion)
- **DTOs**: Schemas de validación (Pydantic)

#### 4. **Infraestructura**
- **Repositories**: Acceso a datos
- **Oracle Connection**: Gestión de conexiones

---

## 🔧 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap.git
cd Proyecto_API_REST_Inacap
```

### 2. Instalar Dependencias

#### Backend (API)
```bash
cd webApiRestFul
pip install -r requirements.txt
```

#### Frontend (PyQt6)
```bash
cd pyqt6
pip install -r requirements.txt
```

### 3. Configurar Base de Datos Oracle

```bash
# Opción 1: Script automático (Windows)
EJECUTAR_SCRIPTS_SQL.bat

# Opción 2: Manual
cd webApiRestFul/sql
sqlplus admin/password@dsn @01_create_tables.sql
# ... ejecutar scripts 02 al 07 en orden
```

📖 **Guía detallada**: [INSTRUCCIONES_BASE_DATOS.md](INSTRUCCIONES_BASE_DATOS.md)

### 4. Configurar Credenciales

Editar `webApiRestFul/config/settings.json`:

```json
{
  "oracle": {
    "user": "admin",
    "password": "TU_PASSWORD",
    "dsn": "basedatos699_medium",
    "wallet_dir": "RUTA_A_TU_WALLET"
  }
}
```

---

## 📊 Estructura del Proyecto

```
Proyecto_API_Rest_Inacap/
├── 1_Iniciar_API.bat              # Script inicio rápido API
├── 2_Iniciar_Cliente.bat          # Script inicio rápido Cliente
├── EJECUTAR_SCRIPTS_SQL.bat       # Script instalación BD
├── fix_password_admin.py          # Utilidad corrección passwords
│
├── webApiRestFul/                 # API REST Backend
│   ├── app/
│   │   ├── domain/models/         # Entidades de dominio
│   │   ├── infrastructure/
│   │   │   ├── database/          # Conexión Oracle
│   │   │   └── repositories/      # Repositorios
│   │   └── api/
│   │       ├── controllers/       # Endpoints HTTP
│   │       ├── services/          # Lógica de negocio
│   │       └── schemas/           # DTOs Pydantic
│   ├── config/
│   │   └── settings.json          # Configuración
│   ├── sql/                       # Scripts SQL
│   │   ├── 01_create_tables.sql
│   │   ├── 02_create_audit_tables.sql
│   │   ├── 03_create_triggers.sql
│   │   ├── 04_create_stored_procedures_crud.sql
│   │   ├── 05_create_stored_procedures_auth.sql
│   │   ├── 06_create_stored_procedures_transactions.sql
│   │   └── 07_insert_sample_data.sql
│   ├── main.py                    # Punto de entrada API
│   └── requirements.txt
│
└── pyqt6/                         # Cliente Desktop
    ├── app/
    │   ├── domain/models/         # Modelos
    │   ├── infrastructure/repositories/  # Repos HTTP
    │   ├── viewmodels/            # ViewModels (MVVM)
    │   └── ui/                    # Interfaz gráfica
    │       ├── login_dialog.py
    │       ├── main_window.py
    │       └── pelicula_form_dialog.py
    ├── config/
    │   └── settings.json
    ├── main.py
    └── requirements.txt
```

---

## 💻 Tecnologías Utilizadas

| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Backend Framework** | FastAPI | 0.110.0 |
| **Frontend Framework** | PyQt6 | 6.6.0 |
| **Database** | Oracle Database | 19c+ |
| **Database Driver** | oracledb | 2.0.1 |
| **Authentication** | PyJWT | 2.8.0 |
| **Validation** | Pydantic | 2.6.1 |
| **ASGI Server** | Uvicorn | - |
| **HTTP Client** | requests | 2.31.0 |
| **Language** | Python | 3.12 |

---

## 📝 Scripts SQL

| Orden | Script | Descripción |
|-------|--------|-------------|
| 1 | `01_create_tables.sql` | 11 tablas principales |
| 2 | `02_create_audit_tables.sql` | 5 tablas de bitácora |
| 3 | `03_create_triggers.sql` | 15 triggers de auditoría |
| 4 | `04_create_stored_procedures_crud.sql` | Procedimientos CRUD |
| 5 | `05_create_stored_procedures_auth.sql` | Procedimientos autenticación |
| 6 | `06_create_stored_procedures_transactions.sql` | Procedimientos transaccionales |
| 7 | `07_insert_sample_data.sql` | Datos de prueba |

---

## 🔐 Credenciales de Prueba

### Usuario Administrador
```
Usuario: admin
Password: admin123
Rol: admin
```

### Usuario Normal
```
Usuario: usuario1
Password: user123
Rol: usuario
```

---

## 📋 Endpoints API

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

### Documentación
- `GET /` - Info de la API
- `GET /health` - Estado del servidor
- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc UI

---

## 🧪 Pruebas

### Probar API con Swagger

1. Ir a http://localhost:8000/docs
2. Click en `POST /auth/login`
3. Click en "Try it out"
4. Ingresar:
   ```json
   {
     "username": "admin",
     "password": "admin123"
   }
   ```
5. Copiar el `access_token`
6. Click en "Authorize" (🔒)
7. Pegar token con prefijo: `Bearer <token>`
8. Probar endpoints de películas

### Probar con PowerShell

```powershell
# Login
$response = Invoke-RestMethod -Uri "http://localhost:8000/auth/login" `
    -Method Post -ContentType "application/json" `
    -Body '{"username":"admin","password":"admin123"}'

$token = $response.access_token

# Listar películas
$headers = @{ "Authorization" = "Bearer $token" }
Invoke-RestMethod -Uri "http://localhost:8000/peliculas/" -Headers $headers
```

---

## 🐛 Troubleshooting

### Error: "Max retries exceeded"
➡️ La API no está corriendo  
✅ Ejecutar `1_Iniciar_API.bat`

### Error: "SP_LOGIN is invalid"
➡️ Stored procedures no existen en BD  
✅ Ejecutar `EJECUTAR_SCRIPTS_SQL.bat`

### Error: "Contraseña incorrecta"
➡️ Passwords no están hasheados  
✅ Ejecutar `FIX_ACTUALIZAR_PASSWORD.bat` o `python fix_password_admin.py`

📖 **Más ayuda**: [INICIO_RAPIDO.md#troubleshooting](INICIO_RAPIDO.md#troubleshooting)

---

## 📚 Patrones de Diseño Implementados

- ✅ **Repository Pattern**: Abstracción acceso a datos
- ✅ **MVVM**: Model-View-ViewModel en PyQt6
- ✅ **Dependency Injection**: FastAPI dependencies
- ✅ **DTO Pattern**: Pydantic schemas
- ✅ **Layered Architecture**: Separación en capas
- ✅ **Factory Pattern**: Creación de conexiones

---

## 🤝 Contribución

Este es un proyecto académico de INACAP. Si deseas contribuir:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es de código abierto para fines educativos.

---

## 👨‍💻 Autor

**Walther Mora Rivera**  
Estudiante - INACAP  
Proyecto: Sistema de Gestión de Festival de Cine

---

## 🔗 Enlaces Útiles

- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [Documentación PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- [Oracle Database Documentation](https://docs.oracle.com/en/database/)
- [Repositorio GitHub](https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap)

---

<div align="center">

**⭐ Si te gustó el proyecto, dale una estrella en GitHub ⭐**

[Reportar Bug](https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap/issues) • [Solicitar Feature](https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap/issues)

</div>
