from PyQt6.QtWidgets import QMainWindow,QMessageBox,QWidget

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui import QAction

class TestMenu(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.stateMItem = QMenu("State")
        self.editMItem = QMenu("Edit")
        self.addMenu(self.stateMItem)
        self.addMenu(self.editMItem)
        self.setMinimumSize(1920,1)

        self.loadMenuAction = QAction("Load")
        self.stateMItem.addAction(self.loadMenuAction)

        self.saveMenuAction = QAction("Save")
        self.stateMItem.addAction(self.saveMenuAction)

        self.savecolors = QAction("Save Colors")
        self.loadcolors = QAction("Load Colors")
        self.dropdownMenu = QMenu("Pick Color")
        self.color_canva_action = QAction("Field Color")
        self.color_x_action = QAction("Color X")
        self.color_o_action = QAction("Color O")
        self.dropdownOption1 = self.dropdownMenu.addAction(self.color_canva_action)
        self.dropdownOption2 = self.dropdownMenu.addAction(self.color_x_action)
        self.dropdownOption3 = self.dropdownMenu.addAction(self.color_o_action)
        self.editMItem.addAction(self.savecolors)
        self.editMItem.addAction(self.loadcolors)
        self.editMItem.addMenu(self.dropdownMenu)


        # Connect event handlers for blocked menu items
        self.color_x_action.triggered.connect(self.parent().canvas.choose_color_x)
        self.color_o_action.triggered.connect(self.parent().canvas.choose_color_o)
        self.color_canva_action.triggered.connect(self.parent().canvas.choose_color_canva)

    def addLoadActionHandler(self, handler):
        self.loadMenuAction.triggered.connect(handler)

    def addSaveColorsActionHandler(self, handler):
        self.savecolors.triggered.connect(handler)

    def addLoadColorsActionHandler(self, handler):
        self.loadcolors.triggered.connect(handler)

    def addSaveActionHandler(self, handler):
        self.saveMenuAction.triggered.connect(handler)


    def showBetaMessage(self, menuItem):
        QMessageBox.information(self, "Beta Version", f"This feature ({menuItem}) is unavailable in the beta version of the game.")
