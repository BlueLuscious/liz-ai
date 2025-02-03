from PyQt5.QtWidgets import QApplication
import sys
from gui.app import LizAi


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LizAi()
    window.show()
    sys.exit(app.exec())
    