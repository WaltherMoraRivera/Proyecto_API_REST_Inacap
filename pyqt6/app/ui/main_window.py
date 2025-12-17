"""
Ventana principal de la aplicación
"""
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QLabel, QHeaderView
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from app.viewmodels.pelicula_viewmodel import PeliculaViewModel
from app.ui.pelicula_form_dialog import PeliculaFormDialog


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación"""
    
    def __init__(self, viewmodel: PeliculaViewModel, usuario: dict):
        super().__init__()
        self._viewmodel = viewmodel
        self._usuario = usuario
        self._setup_ui()
        self._connect_signals()
        
        # Cargar datos iniciales
        self._viewmodel.load_peliculas()
    
    def _setup_ui(self):
        """Configura la interfaz de usuario"""
        self.setWindowTitle("Sistema de Gestión de Festival de Cine - INACAP")
        self.setMinimumSize(1000, 600)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Header
        header_layout = QHBoxLayout()
        
        title = QLabel("Gestión de Películas")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        user_label = QLabel(f"Usuario: {self._usuario['nombre_completo']} ({self._usuario['rol']})")
        header_layout.addWidget(user_label)
        
        main_layout.addLayout(header_layout)
        
        # Botones de acción
        button_layout = QHBoxLayout()
        
        self.refresh_button = QPushButton("🔄 Recargar")
        self.refresh_button.clicked.connect(self._handle_refresh)
        button_layout.addWidget(self.refresh_button)
        
        self.new_button = QPushButton("➕ Nueva Película")
        self.new_button.clicked.connect(self._handle_new)
        button_layout.addWidget(self.new_button)
        
        self.edit_button = QPushButton("✏️ Editar")
        self.edit_button.clicked.connect(self._handle_edit)
        self.edit_button.setEnabled(False)
        button_layout.addWidget(self.edit_button)
        
        self.delete_button = QPushButton("🗑️ Eliminar")
        self.delete_button.clicked.connect(self._handle_delete)
        self.delete_button.setEnabled(False)
        button_layout.addWidget(self.delete_button)
        
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        
        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Título", "País", "Director", "Duración (min)",
            "Género", "Clasificación", "Sinopsis"
        ])
        
        # Configurar tabla
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)
        
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.itemSelectionChanged.connect(self._handle_selection_changed)
        self.table.itemDoubleClicked.connect(self._handle_edit)
        
        main_layout.addWidget(self.table)
        
        # Status bar
        self.statusBar().showMessage("Listo")
        
        central_widget.setLayout(main_layout)
    
    def _connect_signals(self):
        """Conecta signals del viewmodel"""
        self._viewmodel.peliculas_changed.connect(self._update_table)
        self._viewmodel.error_occurred.connect(self._show_error)
        self._viewmodel.success_message.connect(self._show_success)
    
    def _update_table(self, peliculas):
        """Actualiza la tabla con las películas"""
        self.table.setRowCount(0)
        
        for pelicula in peliculas:
            row = self.table.rowCount()
            self.table.insertRow(row)
            
            self.table.setItem(row, 0, QTableWidgetItem(str(pelicula.id_pelicula)))
            self.table.setItem(row, 1, QTableWidgetItem(pelicula.titulo))
            self.table.setItem(row, 2, QTableWidgetItem(pelicula.pais_origen))
            self.table.setItem(row, 3, QTableWidgetItem(pelicula.director))
            self.table.setItem(row, 4, QTableWidgetItem(str(pelicula.duracion_minutos)))
            self.table.setItem(row, 5, QTableWidgetItem(pelicula.genero))
            self.table.setItem(row, 6, QTableWidgetItem(pelicula.clasificacion))
            
            # Sinopsis truncada
            sinopsis = pelicula.sinopsis[:50] + "..." if len(pelicula.sinopsis) > 50 else pelicula.sinopsis
            self.table.setItem(row, 7, QTableWidgetItem(sinopsis))
        
        self.statusBar().showMessage(f"{len(peliculas)} película(s) cargada(s)")
    
    def _handle_selection_changed(self):
        """Maneja cambios en la selección de la tabla"""
        has_selection = len(self.table.selectedItems()) > 0
        self.edit_button.setEnabled(has_selection)
        
        # Solo admin puede eliminar
        is_admin = self._usuario.get('rol') == 'admin'
        self.delete_button.setEnabled(has_selection and is_admin)
    
    def _handle_refresh(self):
        """Maneja el botón de recargar"""
        self.statusBar().showMessage("Cargando...")
        self._viewmodel.load_peliculas()
    
    def _handle_new(self):
        """Maneja el botón de nueva película"""
        dialog = PeliculaFormDialog(parent=self)
        
        if dialog.exec() == dialog.DialogCode.Accepted:
            if dialog.validate():
                pelicula = dialog.get_pelicula()
                self._viewmodel.create_pelicula(pelicula)
            else:
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos obligatorios")
    
    def _handle_edit(self):
        """Maneja el botón de editar"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        
        pelicula = self._viewmodel.peliculas[selected_row]
        dialog = PeliculaFormDialog(pelicula=pelicula, parent=self)
        
        if dialog.exec() == dialog.DialogCode.Accepted:
            if dialog.validate():
                updated_pelicula = dialog.get_pelicula()
                self._viewmodel.update_pelicula(updated_pelicula)
            else:
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos obligatorios")
    
    def _handle_delete(self):
        """Maneja el botón de eliminar"""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            return
        
        pelicula = self._viewmodel.peliculas[selected_row]
        
        reply = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Está seguro que desea eliminar la película '{pelicula.titulo}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self._viewmodel.delete_pelicula(pelicula.id_pelicula)
    
    def _show_error(self, message: str):
        """Muestra un mensaje de error"""
        QMessageBox.critical(self, "Error", message)
        self.statusBar().showMessage("Error")
    
    def _show_success(self, message: str):
        """Muestra un mensaje de éxito"""
        QMessageBox.information(self, "Éxito", message)
        self.statusBar().showMessage(message)
