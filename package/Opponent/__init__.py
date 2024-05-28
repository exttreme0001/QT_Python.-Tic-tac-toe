from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit
import sys
from .Opponents import Opponents

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)

    opponents = Opponents(window)
    layout.addWidget(opponents)

    window.show()
    sys.exit(app.exec())
