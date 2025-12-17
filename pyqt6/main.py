"""
Aplicación principal PyQt6 - Sistema de Gestión de Festival de Cine
"""
import sys
import json
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMessageBox
from app.ui.login_dialog import LoginDialog
from app.ui.main_window import MainWindow
from app.infrastructure.repositories.auth_repository import AuthRepository
from app.infrastructure.repositories.pelicula_repository import PeliculaRepository
from app.viewmodels.pelicula_viewmodel import PeliculaViewModel


def load_config():
    """Carga la configuración desde settings.json"""
    config_path = Path(__file__).parent / "config" / "settings.json"
    
    if not config_path.exists():
        # Crear archivo de configuración por defecto
        config_path.parent.mkdir(exist_ok=True)
        default_config = {
            "api_base_url": "http://localhost:8000"
        }
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    """Función principal"""
    app = QApplication(sys.argv)
    app.setApplicationName("Sistema Festival de Cine")
    app.setOrganizationName("INACAP")
    
    # Cargar configuración
    try:
        config = load_config()
        api_base_url = config.get("api_base_url", "http://localhost:8000")
    except Exception as e:
        QMessageBox.critical(None, "Error", f"Error al cargar configuración: {e}")
        return 1
    
    # Crear repositorio de autenticación
    auth_repo = AuthRepository(api_base_url)
    
    # Variables para almacenar datos del login
    usuario = None
    token = None
    
    def on_login_successful(user, tok):
        nonlocal usuario, token
        usuario = user
        token = tok
    
    # Mostrar diálogo de login
    login_dialog = LoginDialog(auth_repo)
    login_dialog.login_successful.connect(on_login_successful)
    
    if login_dialog.exec() != login_dialog.DialogCode.Accepted:
        return 0  # Usuario canceló el login
    
    # Verificar que se obtuvieron los datos
    if not usuario or not token:
        QMessageBox.critical(None, "Error", "No se pudo obtener información del usuario")
        return 1
    
    # Crear repositorio de películas con token
    pelicula_repo = PeliculaRepository(api_base_url, token)
    
    # Crear viewmodel
    viewmodel = PeliculaViewModel(pelicula_repo)
    
    # Crear y mostrar ventana principal
    main_window = MainWindow(viewmodel, usuario)
    main_window.show()
    
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
