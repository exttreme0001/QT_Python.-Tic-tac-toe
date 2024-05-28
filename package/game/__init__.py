from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys

from .Testgame import TestGame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setFixedSize(500,500)
    layout = QVBoxLayout(window)

    game = TestGame(window)
    layout.addWidget(game)
    window.show()
    sys.exit(app.exec())
