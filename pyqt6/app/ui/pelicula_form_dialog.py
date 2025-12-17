"""
Diálogo de formulario para Películas
"""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QSpinBox, QTextEdit, QComboBox,
    QPushButton, QFormLayout
)
from PyQt6.QtCore import Qt
from app.domain.models.pelicula import Pelicula
from typing import Optional


class PeliculaFormDialog(QDialog):
    """Diálogo para crear/editar películas"""
    
    def __init__(self, pelicula: Optional[Pelicula] = None, parent=None):
        super().__init__(parent)
        self._pelicula = pelicula
        self._setup_ui()
        
        if pelicula:
            self._load_data(pelicula)
    
    def _setup_ui(self):
        """Configura la interfaz de usuario"""
        title = "Editar Película" if self._pelicula else "Nueva Película"
        self.setWindowTitle(title)
        self.setMinimumWidth(500)
        
        layout = QVBoxLayout()
        
        # Formulario
        form_layout = QFormLayout()
        
        # Título
        self.titulo_input = QLineEdit()
        self.titulo_input.setMaxLength(100)
        form_layout.addRow("Título *:", self.titulo_input)
        
        # País
        self.pais_input = QLineEdit()
        self.pais_input.setMaxLength(50)
        form_layout.addRow("País de Origen *:", self.pais_input)
        
        # Director
        self.director_input = QLineEdit()
        self.director_input.setMaxLength(100)
        form_layout.addRow("Director *:", self.director_input)
        
        # Duración
        self.duracion_input = QSpinBox()
        self.duracion_input.setMinimum(1)
        self.duracion_input.setMaximum(500)
        self.duracion_input.setValue(90)
        self.duracion_input.setSuffix(" min")
        form_layout.addRow("Duración *:", self.duracion_input)
        
        # Género
        self.genero_combo = QComboBox()
        self.genero_combo.addItems([
            "Drama", "Comedia", "Acción", "Romance", "Ciencia Ficción",
            "Terror", "Suspenso", "Documental", "Animación", "Fantasía"
        ])
        form_layout.addRow("Género:", self.genero_combo)
        
        # Clasificación
        self.clasificacion_combo = QComboBox()
        self.clasificacion_combo.addItems(["TE", "+7", "+14", "+18"])
        form_layout.addRow("Clasificación:", self.clasificacion_combo)
        
        # Sinopsis
        self.sinopsis_input = QTextEdit()
        self.sinopsis_input.setMaximumHeight(100)
        form_layout.addRow("Sinopsis:", self.sinopsis_input)
        
        layout.addLayout(form_layout)
        
        # Botones
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        save_button = QPushButton("Guardar")
        save_button.setMinimumWidth(100)
        save_button.clicked.connect(self.accept)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton("Cancelar")
        cancel_button.setMinimumWidth(100)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def _load_data(self, pelicula: Pelicula):
        """Carga los datos de una película en el formulario"""
        self.titulo_input.setText(pelicula.titulo)
        self.pais_input.setText(pelicula.pais_origen)
        self.director_input.setText(pelicula.director)
        self.duracion_input.setValue(pelicula.duracion_minutos)
        
        index = self.genero_combo.findText(pelicula.genero)
        if index >= 0:
            self.genero_combo.setCurrentIndex(index)
        
        index = self.clasificacion_combo.findText(pelicula.clasificacion)
        if index >= 0:
            self.clasificacion_combo.setCurrentIndex(index)
        
        self.sinopsis_input.setPlainText(pelicula.sinopsis)
    
    def get_pelicula(self) -> Pelicula:
        """Obtiene los datos del formulario como una Película"""
        id_pelicula = self._pelicula.id_pelicula if self._pelicula else None
        
        return Pelicula(
            id_pelicula=id_pelicula,
            titulo=self.titulo_input.text().strip(),
            pais_origen=self.pais_input.text().strip(),
            director=self.director_input.text().strip(),
            duracion_minutos=self.duracion_input.value(),
            genero=self.genero_combo.currentText(),
            clasificacion=self.clasificacion_combo.currentText(),
            sinopsis=self.sinopsis_input.toPlainText().strip() or "Sin sinopsis disponible"
        )
    
    def validate(self) -> bool:
        """Valida los datos del formulario"""
        if not self.titulo_input.text().strip():
            return False
        if not self.pais_input.text().strip():
            return False
        if not self.director_input.text().strip():
            return False
        return True
