# Cliente PyQt6 - Sistema de Gestión de Festival de Cine

Aplicación de escritorio construida con PyQt6 que consume la API REST para gestión visual de películas.

## Características

- ✅ Interfaz gráfica moderna con PyQt6
- ✅ Login con validación
- ✅ CRUD visual de películas
- ✅ Tabla interactiva
- ✅ Formularios de creación/edición
- ✅ Integración completa con API REST
- ✅ Arquitectura MVVM

## Instalación

```bash
# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

**Credenciales de prueba**:
- Usuario: `admin`
- Contraseña: `admin123`

## Funcionalidades

1. **Login**: Autenticación con usuario y contraseña
2. **Listar**: Tabla con todas las películas
3. **Crear**: Formulario para nueva película
4. **Editar**: Modificar película existente (doble click)
5. **Eliminar**: Borrar película (solo administradores)
6. **Recargar**: Actualizar datos desde la API

## Estructura

```
pyqt6/
├── app/
│   ├── domain/models/          # Entidades
│   ├── infrastructure/         # Repositorios HTTP
│   ├── viewmodels/             # Lógica de presentación
│   └── ui/                     # Interfaces gráficas
│       ├── login_dialog.py
│       ├── main_window.py
│       └── pelicula_form_dialog.py
├── config/                     # Configuración
└── main.py                     # Punto de entrada
```

## Configuración

El archivo `config/settings.json` se crea automáticamente con valores por defecto.

Para cambiar la URL de la API, editar:

```json
{
  "api_base_url": "http://localhost:8000"
}
```

## Requisitos

- Python 3.10+
- API REST ejecutándose en http://localhost:8000
- PyQt6
