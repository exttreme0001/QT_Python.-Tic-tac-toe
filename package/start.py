from PyQt6.QtWidgets import QApplication
from TestWindow import TestWindow
import sys

app = QApplication(sys.argv)
wnd = TestWindow()
wnd.show()
sys.exit(app.exec())
