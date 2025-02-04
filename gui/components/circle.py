from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QSizePolicy, QWidget


class CirculoWidget(QWidget):
    """Widget personalizado para dibujar un círculo azul (la IA)"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(160, 160)  # Un poco más grande para evitar recortes
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(QColor(0, 120, 200))
        pen.setWidth(3)
        painter.setPen(pen)

        size = min(self.width(), self.height()) - 6
        x = (self.width() - size) // 2
        y = (self.height() - size) // 2

        painter.drawEllipse(x, y, size, size)
        