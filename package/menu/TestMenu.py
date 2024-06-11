from PyQt6.QtWidgets import QMainWindow,QMessageBox,QWidget

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction

class TestMenu(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.stateMItem = QMenu("State")
        self.editMItem = QMenu("Edit")
        self.fileMItem = QMenu("File")
        self.addMenu(self.stateMItem)
        self.addMenu(self.editMItem)
        self.addMenu(self.fileMItem)
        self.setMinimumSize(1920,1)

        self.loadMenuAction = QAction("Load")
        self.stateMItem.addAction(self.loadMenuAction)

        self.saveMenuAction = QAction("Save")
        self.stateMItem.addAction(self.saveMenuAction)


        self.dropdownMenu = QMenu("Dropdown")
        self.color_canva_action = QAction("Field Color")
        self.color_x_action = QAction("Color X")
        self.color_o_action = QAction("Color O")
        self.dropdownOption1 = self.dropdownMenu.addAction(self.color_canva_action)
        self.dropdownOption2 = self.dropdownMenu.addAction(self.color_x_action)
        self.dropdownOption3 = self.dropdownMenu.addAction(self.color_o_action)
        self.editMItem.addMenu(self.dropdownMenu)

        self.editMItem.addMenu(self.dropdownMenu)

        self.openFileAction = QAction("Open")
        self.fileMItem.addAction(self.openFileAction)


        # Block clicking on menu items
        self.openFileAction.setEnabled(False)

        # Connect event handlers for blocked menu items
        self.openFileAction.triggered.connect(lambda: self.showBetaMessage("Open"))
        self.color_x_action.triggered.connect(self.parent().canvas.choose_color_x)
        self.color_o_action.triggered.connect(self.parent().canvas.choose_color_o)
        self.color_canva_action.triggered.connect(self.parent().canvas.choose_color_canva)

    def addLoadActionHandler(self, handler):
        self.loadMenuAction.triggered.connect(handler)

    def addSaveActionHandler(self, handler):
        self.saveMenuAction.triggered.connect(handler)

    def addOpenFileActionHandler(self, handler):
        self.openFileAction.triggered.connect(handler)

    def showBetaMessage(self, menuItem):
        QMessageBox.information(self, "Beta Version", f"This feature ({menuItem}) is unavailable in the beta version of the game.")
