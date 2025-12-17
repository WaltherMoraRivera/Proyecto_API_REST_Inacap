# Proyecto API con PyQt6 y FastAPI

> **Plantilla de arquitectura empresarial** para aplicaciones Python que integran una API REST (FastAPI) y una interfaz gráfica de escritorio (PyQt6) con conexión a Oracle Database.

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Arquitectura del Proyecto](#-arquitectura-del-proyecto)
- [Estructura de Directorios](#-estructura-de-directorios)
- [Componentes del Proyecto](#-componentes-del-proyecto)
- [Patrones de Diseño](#-patrones-de-diseño)
- [Configuración e Instalación](#-configuración-e-instalación)
- [Guía de Uso](#-guía-de-uso)
- [Usar como Plantilla](#-usar-como-plantilla)
- [Contribución](#-contribución)

---

## 🎯 Descripción General

Este proyecto implementa una **arquitectura de software multicapa** que separa responsabilidades en dos aplicaciones independientes pero interconectadas:

1. **Backend API REST** (FastAPI) - Servidor que expone endpoints HTTP para operaciones CRUD
2. **Frontend Desktop** (PyQt6) - Aplicación de escritorio que consume la API REST

### Características Principales

- ✅ **Arquitectura en capas** (Domain, Infrastructure, Application, Presentation)
- ✅ **Patrón MVVM** en la aplicación PyQt6
- ✅ **Inyección de dependencias** y separación de concerns
- ✅ **Repository Pattern** para abstracción de acceso a datos
- ✅ **API RESTful** con documentación automática (Swagger/OpenAPI)
- ✅ **Validación de datos** con Pydantic
- ✅ **Conexión a Oracle Database** con soporte para Oracle Autonomous Database
- ✅ **Configuración externalizada** (JSON)
- ✅ **Type hints** completos para mejor IDE support

---

## 🏗️ Arquitectura del Proyecto

### Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                     USUARIO FINAL                            │
└──────────────────────┬──────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
┌───────▼────────┐           ┌────────▼────────┐
│  PyQt6 Client  │           │   Web Browser   │
│  (Desktop UI)  │           │  (API Docs)     │
└───────┬────────┘           └────────┬────────┘
        │                             │
        │  HTTP Requests              │
        └──────────────┬──────────────┘
                       │
              ┌────────▼────────┐
              │   FastAPI       │
              │   Application   │
              │  (Port 8000)    │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │ Oracle Database │
              │   (Cloud/Local) │
              └─────────────────┘
```

### Arquitectura en Capas

Ambos proyectos siguen una arquitectura en capas inspirada en **Clean Architecture** y **DDD (Domain-Driven Design)**:

#### 1. **Domain Layer** (Capa de Dominio)
   - **Responsabilidad**: Modelos de negocio puros, sin dependencias externas
   - **Ubicación**: `app/domain/models/`
   - **Ejemplo**: `VistaFalsa` - Entidad de dominio con atributos y validaciones básicas

#### 2. **Infrastructure Layer** (Capa de Infraestructura)
   - **Responsabilidad**: Implementación de acceso a datos, conexiones externas
   - **Ubicación**: `app/infrastructure/`
   - **Componentes**:
     - `repositories/` - Implementación del Repository Pattern
     - `database/` - Gestión de conexiones a BD

#### 3. **Application Layer** (Capa de Aplicación)
   - **Responsabilidad**: Lógica de negocio y casos de uso
   - **Ubicación**: `app/api/services/` (FastAPI) o `app/viewmodels/` (PyQt6)
   - **Componentes**:
     - Services - Orquestación de casos de uso
     - ViewModels - Lógica de presentación

#### 4. **Presentation Layer** (Capa de Presentación)
   - **Responsabilidad**: Interfaz de usuario y controladores HTTP
   - **Ubicación**: `app/api/controllers/` (FastAPI) o `app/ui/` (PyQt6)

---

## 📁 Estructura de Directorios

### Proyecto completo

```
proyectoPyqt6ApiRest/
│
├── pyqt6/                          # Aplicación de escritorio PyQt6
│   ├── app/
│   │   ├── domain/
│   │   │   └── models/             # Entidades de dominio
│   │   │       └── vista_falsa.py
│   │   │
│   │   ├── infrastructure/
│   │   │   └── repositories/       # Implementación de repositorios
│   │   │       └── vista_falsa_repository.py
│   │   │
│   │   ├── viewmodels/             # ViewModels (Lógica de presentación)
│   │   │   └── vista_falsa_viewmodel.py
│   │   │
│   │   ├── ui/                     # Componentes de UI
│   │   │   ├── main_window.py      # Ventana principal
│   │   │   ├── dialogs.py          # Diálogos (formularios, confirmaciones)
│   │   │   ├── delegates.py        # Delegates para QTableView
│   │   │   └── vista_table_model.py # TableModel personalizado
│   │   │
│   │   └── configuration.py        # Gestión de configuración
│   │
│   ├── config/
│   │   └── settings.json           # Configuración (URL API, etc.)
│   │
│   ├── tools/
│   │   └── db_check.py             # Herramientas de diagnóstico
│   │
│   ├── main.py                     # Punto de entrada de la aplicación
│   ├── requirements.txt            # Dependencias Python
│   └── README.md                   # Documentación específica
│
└── webApiRestFul/                  # API REST FastAPI
    ├── app/
    │   ├── domain/
    │   │   └── models/             # Entidades de dominio
    │   │       └── vista_falsa.py
    │   │
    │   ├── infrastructure/
    │   │   ├── database/           # Gestión de conexiones DB
    │   │   │   └── oracle_connection.py
    │   │   └── repositories/       # Implementación de repositorios
    │   │       └── vista_falsa_repository.py
    │   │
    │   ├── api/
    │   │   ├── controllers/        # Controladores (Routers FastAPI)
    │   │   │   └── vista_falsa_controller.py
    │   │   │
    │   │   ├── services/           # Servicios (Lógica de negocio)
    │   │   │   └── vista_falsa_service.py
    │   │   │
    │   │   └── schemas/            # Esquemas Pydantic (DTOs)
    │   │       └── vista_falsa_schema.py
    │   │
    │   └── viewmodels/             # ViewModels (opcional para API)
    │       └── vista_falsa_viewmodel.py
    │
    ├── config/
    │   └── settings.json           # Configuración (DB, etc.)
    │
    ├── sql/
    │   └── script.sql              # Scripts de base de datos
    │
    ├── Wallet/                     # Wallet de Oracle (ignorado en git)
    │
    ├── main.py                     # Punto de entrada (desarrollo)
    ├── api_main.py                 # Punto de entrada (producción)
    ├── requirements.txt            # Dependencias Python
    └── README.md                   # Documentación específica
```

---

## 🔧 Componentes del Proyecto

### 1. **webApiRestFul** - API REST con FastAPI

#### 1.1 Controllers (Controladores)

**Archivo**: `app/api/controllers/vista_falsa_controller.py`

Los controladores son **routers de FastAPI** que definen los endpoints HTTP:

```python
@router.get("/", response_model=List[VistaFalsaSchema])
def get_all():
    """Obtener todos los registros"""
    return service.get_all()

@router.post("/", status_code=201)
def create(data: VistaFalsaCreateSchema):
    """Crear un nuevo registro"""
    vista = VistaFalsa(id_vista=None, **data.model_dump())
    service.create(vista)
    return {"message": "Creado correctamente"}
```

**Responsabilidades**:
- Definir rutas y métodos HTTP
- Validar datos de entrada con Pydantic
- Delegar lógica de negocio a Services
- Formatear respuestas HTTP

#### 1.2 Services (Servicios)

**Archivo**: `app/api/services/vista_falsa_service.py`

Capa de lógica de negocio que orquesta operaciones:

```python
class VistaFalsaService:
    def __init__(self):
        self.repo = VistaFalsaRepository()
    
    def get_all(self) -> List[VistaFalsa]:
        return self.repo.get_all()
    
    def create(self, vista: VistaFalsa):
        # Aquí se puede agregar validaciones de negocio
        return self.repo.add(vista)
```

**Responsabilidades**:
- Implementar casos de uso
- Validaciones de negocio complejas
- Coordinación entre múltiples repositorios
- Transformación de datos

#### 1.3 Schemas (DTOs - Data Transfer Objects)

**Archivo**: `app/api/schemas/vista_falsa_schema.py`

Definen la estructura de datos de entrada/salida de la API:

```python
class VistaFalsaCreateSchema(BaseModel):
    """Payload para crear un registro (sin ID)"""
    estudiante_nombre: str
    nivel_educativo: str
    # ... otros campos

class VistaFalsaSchema(BaseModel):
    """Payload completo con ID"""
    id_vista: Optional[int]
    estudiante_nombre: str
    # ... otros campos
    
    class Config:
        from_attributes = True  # Permite conversión desde objetos ORM
```

#### 1.4 Repository (Repositorios)

**Archivo**: `app/infrastructure/repositories/vista_falsa_repository.py`

Abstrae el acceso a datos:

```python
class VistaFalsaRepository:
    def get_all(self) -> List[VistaFalsa]:
        # Ejecuta SQL y convierte resultados a objetos de dominio
        
    def get_by_id(self, vista_id: int) -> Optional[VistaFalsa]:
        # Consulta específica
        
    def add(self, vista: VistaFalsa):
        # INSERT
        
    def update(self, vista: VistaFalsa):
        # UPDATE
        
    def delete(self, vista_id: int):
        # DELETE
```

#### 1.5 Database Connection

**Archivo**: `app/infrastructure/database/oracle_connection.py`

Gestiona conexiones a Oracle Database:

```python
class OracleConnection:
    """Encapsula la conexión a Oracle Autonomous Database"""
    
    def __init__(self, user, password, dsn, wallet_dir=None):
        # Configuración de conexión
        
    def get_connection(self) -> oracledb.Connection:
        # Retorna una conexión activa
        
    @classmethod
    def from_settings_file(cls, path: Path):
        # Factory method para crear desde archivo de configuración
```

**Características**:
- Soporte para Oracle Autonomous Database con Wallet
- Manejo de thick/thin mode
- Pool de conexiones
- Configuración desde JSON

---

### 2. **pyqt6** - Aplicación de Escritorio

#### 2.1 MVVM Pattern (Model-View-ViewModel)

**View** → **ViewModel** → **Model** (Repository)

##### View (main_window.py)

```python
class MainWindow(QMainWindow):
    """Ventana principal - Vista"""
    
    def __init__(self):
        self._viewmodel = VistaFalsaViewModel(repository)
        self._model = VistaTableModel()
        self._setup_ui()
        self._connect_signals()
```

**Responsabilidades**:
- Renderizar UI
- Capturar eventos de usuario
- Enlazar con ViewModel mediante signals/slots

##### ViewModel (vista_falsa_viewmodel.py)

```python
class VistaFalsaViewModel(QObject):
    """ViewModel - Lógica de presentación"""
    
    vistas_changed = pyqtSignal(list)  # Signal para notificar cambios
    error_occurred = pyqtSignal(str)
    
    def load_vistas(self):
        """Cargar datos desde el repositorio"""
        try:
            vistas = self._repository.get_all()
            self.vistas_changed.emit(vistas)
        except Exception as e:
            self.error_occurred.emit(str(e))
```

**Responsabilidades**:
- Gestionar estado de la aplicación
- Orquestar llamadas al repositorio
- Notificar cambios a la vista mediante signals
- Manejar errores

##### Model (vista_table_model.py)

```python
class VistaTableModel(QAbstractTableModel):
    """TableModel para Qt - Adaptador de datos"""
    
    def data(self, index, role):
        """Retorna datos para cada celda"""
        
    def update_vistas(self, vistas: List[VistaFalsa]):
        """Actualiza los datos y notifica a la vista"""
        self.beginResetModel()
        self._vistas = vistas
        self.endResetModel()
```

#### 2.2 Dialogs (Diálogos)

**Archivo**: `app/ui/dialogs.py`

Ventanas modales para formularios:

```python
class VistaFormDialog(QDialog):
    """Formulario para crear/editar registros"""
    
    def get_data(self) -> dict:
        """Retorna datos del formulario"""
```

#### 2.3 Delegates (Delegados)

**Archivo**: `app/ui/delegates.py`

Renderizado personalizado en celdas de tabla:

```python
class DetailButtonDelegate(QStyledItemDelegate):
    """Renderiza un botón en cada fila"""
    
    def paint(self, painter, option, index):
        """Dibuja el botón"""
```

#### 2.4 Repository (Cliente HTTP)

**Archivo**: `app/infrastructure/repositories/vista_falsa_repository.py`

Consume la API REST:

```python
class VistaFalsaRepository:
    def __init__(self, api_base_url: str):
        self._base_url = api_base_url
    
    def get_all(self) -> List[VistaFalsa]:
        response = requests.get(f"{self._base_url}/vista-falsa/")
        return [VistaFalsa(**item) for item in response.json()]
```

---

## 🎨 Patrones de Diseño

### 1. **Repository Pattern**
Abstrae el acceso a datos, permitiendo cambiar la fuente de datos sin afectar la lógica de negocio.

### 2. **MVVM (Model-View-ViewModel)**
Separa la lógica de presentación de la UI, facilitando testing y mantenibilidad.

### 3. **Dependency Injection**
Los objetos reciben sus dependencias desde fuera:
```python
repository = VistaFalsaRepository(api_base_url)
viewmodel = VistaFalsaViewModel(repository)
```

### 4. **Factory Pattern**
Creación de objetos mediante métodos factory:
```python
OracleConnection.from_settings_file(Path("config/settings.json"))
```

### 5. **DTO (Data Transfer Object)**
Schemas de Pydantic para transferencia de datos entre capas.

### 6. **Separation of Concerns**
Cada clase tiene una responsabilidad única y bien definida.

---

## ⚙️ Configuración e Instalación

### Requisitos del Sistema

- **Python**: 3.10 o superior (recomendado 3.11+)
- **Oracle Database**: 19c o superior / Oracle Autonomous Database
- **Oracle Instant Client**: 19.x o superior (para thick mode)
- **Sistema Operativo**: Windows, Linux o macOS

### Instalación Paso a Paso

#### 1. Clonar el repositorio

```bash
git clone https://github.com/WaltherMoraRivera/Proyecto_API_Progra_Objetos.git
cd Proyecto_API_Progra_Objetos
```

#### 2. Configurar el Backend (webApiRestFul)

```bash
cd webApiRestFul

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

**Configurar `config/settings.json`**:

```json
{
  "oracle": {
    "user": "ADMIN",
    "password": "TuPassword123",
    "dsn": "tu_servicio_high",
    "wallet_dir": "Wallet",
    "wallet_password": null
  }
}
```

**Colocar Wallet de Oracle** (si usas Autonomous Database):
- Descargar el Wallet desde Oracle Cloud
- Extraer en la carpeta `Wallet/`

#### 3. Configurar el Frontend (pyqt6)

```bash
cd ../pyqt6

# Crear entorno virtual independiente
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

**Configurar `config/settings.json`**:

```json
{
  "api_base_url": "http://localhost:8000"
}
```

#### 4. Crear la base de datos

Ejecutar el script SQL en Oracle:

```bash
cd ../webApiRestFul
# Usar SQL Developer, SQL*Plus o similar
sqlplus ADMIN/password@tu_servicio_high @sql/script.sql
```

---

## 🚀 Guía de Uso

### Iniciar la API (Backend)

```bash
cd webApiRestFul
python main.py
```

La API estará disponible en:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/vista-falsa/` | Listar todos |
| GET | `/vista-falsa/{id}` | Obtener por ID |
| POST | `/vista-falsa/` | Crear nuevo |
| PUT | `/vista-falsa/{id}` | Actualizar |
| DELETE | `/vista-falsa/{id}` | Eliminar |

### Iniciar la Aplicación Desktop (Frontend)

```bash
cd pyqt6
python main.py
```

### Funcionalidades de la UI

1. **Listar registros**: Tabla con todos los datos
2. **Crear**: Botón "Nuevo" → Formulario
3. **Editar**: Seleccionar fila → Botón "Editar"
4. **Eliminar**: Seleccionar fila(s) → Botón "Eliminar"
5. **Ver detalles**: Botón "👁" en cada fila
6. **Recargar**: Botón "Recargar" para actualizar datos

---

## 📚 Usar como Plantilla

### Para crear un nuevo proyecto basado en esta arquitectura:

#### 1. **Clonar y renombrar**

```bash
git clone https://github.com/WaltherMoraRivera/Proyecto_API_Progra_Objetos.git MiNuevoProyecto
cd MiNuevoProyecto
rm -rf .git
git init
```

#### 2. **Adaptar el modelo de dominio**

Supongamos que quieres gestionar "Productos":

**En `webApiRestFul/app/domain/models/`**:

Crear `producto.py`:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    id_producto: Optional[int]
    nombre: str
    descripcion: str
    precio: float
    stock: int
```

#### 3. **Crear el schema Pydantic**

**En `webApiRestFul/app/api/schemas/`**:

Crear `producto_schema.py`:
```python
from pydantic import BaseModel
from typing import Optional

class ProductoCreateSchema(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int

class ProductoSchema(ProductoCreateSchema):
    id_producto: Optional[int]
    
    class Config:
        from_attributes = True
```

#### 4. **Implementar el repositorio**

**En `webApiRestFul/app/infrastructure/repositories/`**:

Copiar `vista_falsa_repository.py` → `producto_repository.py`

Adaptar las consultas SQL:
```python
def get_all(self) -> List[Producto]:
    with self._connection.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id_producto, nombre, descripcion, precio, stock FROM productos")
        rows = cursor.fetchall()
        return [Producto(*row) for row in rows]
```

#### 5. **Crear el servicio**

**En `webApiRestFul/app/api/services/`**:

Copiar y adaptar `producto_service.py`

#### 6. **Crear el controlador**

**En `webApiRestFul/app/api/controllers/`**:

Copiar `vista_falsa_controller.py` → `producto_controller.py`

Cambiar:
- Nombre del router: `router = APIRouter(prefix="/productos", tags=["Productos"])`
- Reemplazar referencias a `VistaFalsa` por `Producto`

#### 7. **Registrar el router en `main.py`**

```python
from app.api.controllers.producto_controller import router as producto_router

app = FastAPI()
app.include_router(producto_router)
```

#### 8. **Adaptar el frontend PyQt6**

Replicar la misma estructura en `pyqt6/app/`:
- Modelo de dominio
- Repository (cliente HTTP)
- ViewModel
- UI (MainWindow, Dialogs, TableModel)

---

## 🔄 Flujo de Datos

### Creación de un registro (POST)

```
Usuario → [PyQt6 Form Dialog]
              ↓
         [ViewModel.add()]
              ↓
         [Repository HTTP Client]
              ↓  HTTP POST
         [FastAPI Controller]
              ↓
         [Service.create()]
              ↓
         [Repository.add()]
              ↓
         [Oracle Database]
              ↓
         [Response 201]
              ↓
         [ViewModel emite signal]
              ↓
         [View actualiza tabla]
```

---

## 📝 Buenas Prácticas Implementadas

### 1. **Type Hints**
Todo el código usa type hints para mejor IDE support y detección de errores.

### 2. **Docstrings**
Todas las clases y métodos públicos están documentados.

### 3. **Separación de Configuración**
Credenciales y configuración en archivos JSON externos (no en código).

### 4. **Manejo de Errores**
Try-except en puntos críticos con propagación de errores a la UI.

### 5. **Signals/Slots en PyQt6**
Comunicación desacoplada entre componentes.

### 6. **Validación de Datos**
Pydantic valida automáticamente datos de entrada/salida en la API.

### 7. **Documentación Automática**
FastAPI genera docs interactivas en `/docs`.

### 8. **.gitignore**
Excluye archivos sensibles (Wallet, settings.json, __pycache__).

---

## 🧪 Testing (Próximos pasos)

### Estructura recomendada para tests:

```
tests/
├── unit/
│   ├── test_models.py
│   ├── test_services.py
│   └── test_repositories.py
├── integration/
│   └── test_api_endpoints.py
└── e2e/
    └── test_ui_flow.py
```

### Librerías recomendadas:
- `pytest` - Framework de testing
- `pytest-cov` - Cobertura de código
- `httpx` - Cliente HTTP async para tests de API
- `pytest-qt` - Testing de PyQt6

---

## 📦 Dependencias Completas

### webApiRestFul

```txt
fastapi==0.110.0          # Framework web asíncrono
uvicorn[standard]==0.29.0 # Servidor ASGI
oracledb==2.0.1           # Driver de Oracle
python-dotenv==1.0.1      # Gestión de variables de entorno
pydantic==2.x             # Validación de datos
```

### pyqt6

```txt
PyQt6>=6.5.0              # Framework GUI
requests>=2.31.0          # Cliente HTTP
python-dotenv>=1.0.0      # Gestión de configuración
```

---

## 🤝 Contribución

### Para contribuir a este proyecto:

1. Fork el repositorio
2. Crear una rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m "Agrega nueva funcionalidad"`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crear Pull Request

### Convenciones de código:

- Seguir **PEP 8** (Python Style Guide)
- Usar **type hints** en todas las funciones
- Documentar con **docstrings** (Google style)
- Nombres en **español** para dominio de negocio
- Nombres en **inglés** para infraestructura técnica

---

## 📄 Licencia

Proyecto académico - INACAP 2025

**Propósito educativo**: Este proyecto es una plantilla de referencia para aprender arquitectura de software en Python.

---

## 🙏 Agradecimientos

- **INACAP** - Asignatura de Programación de Objetos
- **FastAPI** - Framework moderno para APIs
- **Qt/PyQt6** - Framework multiplataforma para GUIs
- **Oracle** - Base de datos empresarial

---

## 📞 Contacto y Soporte

Para preguntas, issues o sugerencias:
- **GitHub Issues**: [Crear issue](https://github.com/WaltherMoraRivera/Proyecto_API_Progra_Objetos/issues)
- **Repositorio**: https://github.com/WaltherMoraRivera/Proyecto_API_Progra_Objetos

---

**¡Feliz codificación! 🚀**
