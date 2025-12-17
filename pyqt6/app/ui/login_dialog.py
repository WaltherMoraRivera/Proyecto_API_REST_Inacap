"""
Ventana de Login
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont


class LoginDialog(QDialog):
    """Diálogo de login"""
    
    login_successful = pyqtSignal(dict, str)  # usuario, token
    
    def __init__(self, auth_repository):
        super().__init__()
        self._auth_repository = auth_repository
        self._setup_ui()
    
    def _setup_ui(self):
        """Configura la interfaz de usuario"""
        self.setWindowTitle("Login - Sistema Festival de Cine")
        self.setMinimumWidth(400)
        self.setMinimumHeight(250)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        
        # Título
        title = QLabel("Sistema de Gestión\nFestival de Cine")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        layout.addSpacing(20)
        
        # Usuario
        username_layout = QHBoxLayout()
        username_label = QLabel("Usuario:")
        username_label.setMinimumWidth(80)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Ingrese su usuario")
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        layout.addLayout(username_layout)
        
        # Contraseña
        password_layout = QHBoxLayout()
        password_label = QLabel("Contraseña:")
        password_label.setMinimumWidth(80)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Ingrese su contraseña")
        self.password_input.returnPressed.connect(self._handle_login)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)
        
        layout.addSpacing(20)
        
        # Botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.login_button = QPushButton("Iniciar Sesión")
        self.login_button.setMinimumWidth(120)
        self.login_button.clicked.connect(self._handle_login)
        button_layout.addWidget(self.login_button)
        
        cancel_button = QPushButton("Cancelar")
        cancel_button.setMinimumWidth(120)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        # Info
        info_label = QLabel("Usuario de prueba: admin / admin123")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info_label.setStyleSheet("color: gray; font-size: 10px;")
        layout.addWidget(info_label)
        
        self.setLayout(layout)
    
    def _handle_login(self):
        """Maneja el evento de login"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña")
            return
        
        # Deshabilitar botón mientras se procesa
        self.login_button.setEnabled(False)
        self.login_button.setText("Validando...")
        
        # Realizar login
        success, usuario, token, error_msg = self._auth_repository.login(username, password)
        
        # Rehabilitar botón
        self.login_button.setEnabled(True)
        self.login_button.setText("Iniciar Sesión")
        
        if success:
            self.login_successful.emit(usuario, token)
            self.accept()
        else:
            QMessageBox.critical(self, "Error de Login", error_msg or "Credenciales inválidas")
            self.password_input.clear()
            self.password_input.setFocus()
