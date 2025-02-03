from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget
)
from gui.components.circle import CirculoWidget
import qtawesome as qta


class LizAi(QMainWindow):
    """Ventana principal"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liz")
        self.setGeometry(100, 100, 300, 500)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # 📌 Espaciador superior para empujar el círculo al centro
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # 📌 Widget del círculo (IA)
        self.circulo = CirculoWidget()
        layout.addWidget(self.circulo, alignment=Qt.AlignmentFlag.AlignCenter)

        # 📌 Otro espaciador para separar el botón
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # 📌 Botón de micrófono
        self.boton = QPushButton()
        self.boton.setFixedSize(100, 50)  # Tamaño fijo del botón
        self.boton.setIcon(qta.icon("fa.microphone", color="white"))
        self.boton.setIconSize(self.boton.size() * 0.5)
        self.boton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.boton.setStyleSheet(
            "background-color:rgb(0, 120, 200); color:white; border-radius:8px; padding:5px;"
        )
        # self.boton.clicked.connect()

        layout.addWidget(self.boton, alignment=Qt.AlignmentFlag.AlignCenter)

        # 📌 Espaciador inferior para ajustar
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
