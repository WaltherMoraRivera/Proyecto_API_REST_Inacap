# 📋 CHANGELOG - Sistema Festival de Cine

## [1.0.0] - 2025-12-17

### ✅ Implementado

#### 🗄️ Base de Datos
- ✅ 11 tablas principales (PELICULA, FUNCION, USUARIO, SEDE, CIUDAD, etc.)
- ✅ 5 tablas de auditoría (bitácoras)
- ✅ 15 triggers para auditoría automática (INSERT, UPDATE, DELETE)
- ✅ 15+ stored procedures para CRUD, autenticación y transacciones
- ✅ Datos de prueba (usuario admin, películas, salas, funciones)

#### 🔧 API REST (FastAPI)
- ✅ Autenticación JWT (60 minutos de expiración)
- ✅ Endpoints de autenticación (/auth/login, /register, /logout)
- ✅ Endpoints CRUD de películas (/peliculas)
- ✅ Middleware CORS configurado
- ✅ Documentación automática Swagger (/docs)
- ✅ Control de acceso basado en roles
- ✅ Manejo de errores centralizado

#### 🖥️ Cliente PyQt6
- ✅ Ventana de login con validación
- ✅ Interfaz principal con tabla de películas
- ✅ Formularios para crear/editar películas
- ✅ Confirmación de eliminación
- ✅ Manejo de errores con diálogos visuales
- ✅ Integración completa con API REST

#### 📦 Configuración y Deploy
- ✅ Archivos batch para inicio rápido (Windows)
- ✅ Configuración JSON para credenciales
- ✅ Soporte para Oracle Autonomous Database
- ✅ Scripts de instalación y ejecución
- ✅ Documentación completa

### 🐛 Bugs Corregidos

#### Fix #1: Contraseñas en texto plano
- **Problema**: Las contraseñas en la BD estaban sin hashear
- **Solución**: Actualizado script SQL para usar SHA-256 hash
- **Archivos**: 
  - `webApiRestFul/sql/07_insert_sample_data.sql`
  - `fix_password_admin.py` (script de corrección)
  - `webApiRestFul/sql/FIX_actualizar_password_admin.sql`

#### Fix #2: Error de inicialización del cliente
- **Problema**: Signal `login_successful` no se capturaba correctamente
- **Solución**: Conectar signal ANTES de ejecutar el diálogo
- **Archivo**: `pyqt6/main.py`

#### Fix #3: Error 500 al cargar películas
- **Problema**: Mal manejo de cursor de referencia en repositorio
- **Solución**: Corrección en llamada a stored procedure y manejo de resultados
- **Archivo**: `webApiRestFul/app/infrastructure/repositories/pelicula_repository.py`

#### Fix #4: Campo sinopsis no opcional
- **Problema**: Modelo requería sinopsis obligatorio
- **Solución**: Campo sinopsis marcado como Optional
- **Archivo**: `webApiRestFul/app/domain/models/pelicula.py`

### 📝 Archivos Creados

#### Scripts de Utilidad
- `1_Iniciar_API.bat` - Inicia la API FastAPI
- `2_Iniciar_Cliente.bat` - Inicia el cliente PyQt6
- `EJECUTAR_SCRIPTS_SQL.bat` - Ejecuta todos los scripts SQL
- `FIX_ACTUALIZAR_PASSWORD.bat` - Corrige passwords hasheados
- `fix_password_admin.py` - Script Python para actualizar passwords

#### Documentación
- `INICIO_RAPIDO.md` - Guía de inicio rápido
- `INSTRUCCIONES_BASE_DATOS.md` - Instrucciones para configurar BD
- `CHANGELOG.md` - Registro de cambios (este archivo)

### 🔐 Credenciales de Prueba

```
Usuario: admin
Password: admin123
Rol: admin

Usuario: usuario1
Password: user123
Rol: usuario
```

### 🏗️ Arquitectura Implementada

```
┌─────────────┐      HTTP/REST      ┌──────────────┐      SQL       ┌─────────────┐
│   PyQt6     │────────────────────►│   FastAPI    │───────────────►│   Oracle    │
│   Client    │◄────────────────────│     API      │◄───────────────│  Database   │
└─────────────┘     JSON + JWT      └──────────────┘   Procedures   └─────────────┘
```

**Capas**:
- **Presentación**: PyQt6 (MVVM pattern)
- **Aplicación**: FastAPI controllers + services
- **Dominio**: Models + DTOs
- **Infraestructura**: Repositories + Oracle connection

### 📊 Estadísticas del Proyecto

- **Archivos SQL**: 8 scripts
- **Líneas de código Python (API)**: ~1,500
- **Líneas de código Python (Cliente)**: ~800
- **Stored Procedures**: 15+
- **Triggers**: 15
- **Tablas**: 16 (11 principales + 5 auditoría)
- **Endpoints API**: 10+

### 🚀 Próximas Mejoras (v1.1.0)

- [ ] Gestión de funciones y proyecciones
- [ ] Módulo de asistentes
- [ ] Gestión de jurados y evaluaciones
- [ ] Sistema de premiación
- [ ] Reportes y estadísticas
- [ ] Exportación a PDF/Excel
- [ ] Dashboard administrativo
- [ ] Mejoras en UX/UI

### 🔗 Recursos

- **Repositorio**: https://github.com/WaltherMoraRivera/Proyecto_API_REST_Inacap.git
- **Oracle Database**: basedatos699_medium (Autonomous)
- **Puerto API**: 8000
- **Framework Frontend**: PyQt6 6.6.0
- **Framework Backend**: FastAPI 0.110.0

---

## Notas de Desarrollo

### Tecnologías Utilizadas
- Python 3.12
- FastAPI 0.110.0
- PyQt6 6.6.0
- Oracle Database 19c+ (Autonomous)
- oracledb 2.0.1 (driver Python)
- PyJWT 2.8.0
- Pydantic 2.6.1
- Uvicorn (ASGI server)

### Patrones de Diseño
- **Repository Pattern**: Abstracción de acceso a datos
- **MVVM**: Separación UI/lógica en cliente PyQt6
- **Dependency Injection**: FastAPI dependencies
- **DTO Pattern**: Schemas Pydantic para validación

### Seguridad Implementada
- ✅ Autenticación JWT
- ✅ Hashing SHA-256 para contraseñas
- ✅ Validación de entrada con Pydantic
- ✅ CORS configurado
- ✅ Auditoría en base de datos
- ✅ Control de acceso por roles

---

**Mantenido por**: Walther Mora Rivera  
**Institución**: INACAP  
**Fecha**: Diciembre 2025
