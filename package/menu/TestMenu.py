from PyQt6.QtWidgets import QMainWindow,QMessageBox

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction

class TestMenu(QMenuBar):
    def __init__(self, parent: QMainWindow):
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
        self.dropdownOption1 = self.dropdownMenu.addAction("Option 1")
        self.dropdownOption2 = self.dropdownMenu.addAction("Option 2")
        self.dropdownOption3 = self.dropdownMenu.addAction("Option 3")
        self.editMItem.addMenu(self.dropdownMenu)

        self.editMItem.addMenu(self.dropdownMenu)

        self.openFileAction = QAction("Open")
        self.fileMItem.addAction(self.openFileAction)


        # Block clicking on menu items
        self.openFileAction.setEnabled(False)

        # Connect event handlers for blocked menu items
        self.dropdownOption1.triggered.connect(lambda: self.showBetaMessage("Option 1"))
        self.dropdownOption2.triggered.connect(lambda: self.showBetaMessage("Option 2"))
        self.dropdownOption3.triggered.connect(lambda: self.showBetaMessage("Option 3"))
        self.openFileAction.triggered.connect(lambda: self.showBetaMessage("Open"))


    def addLoadActionHandler(self, handler):
        self.loadMenuAction.triggered.connect(handler)

    def addSaveActionHandler(self, handler):
        self.saveMenuAction.triggered.connect(handler)

    def addOpenFileActionHandler(self, handler):
        self.openFileAction.triggered.connect(handler)

    def showBetaMessage(self, menuItem):
        QMessageBox.information(self, "Beta Version", f"This feature ({menuItem}) is unavailable in the beta version of the game.")
