from PyQt6.QtWidgets import QPushButton, QWidget, QGridLayout
from PyQt6.QtGui import QFont
class GameBlock(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.gamebox = QGridLayout(self)
        self.gamebox.setSpacing(7)
        self.buttons = []  # A list for storing buttons
        self.BigSymbolDraw=0
        self.player_turn = True  # Variable for tracking the player's progress
        self.createButtons()
        self.draw=1
        self.NeedToSayAbDraw=0
        self.Win= ""
        self.WinButton = QPushButton(self.Win)


    def createButtons(self):
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                self.buttons.append(button)
                button.setFixedSize(47, 47)
                button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
                button.clicked.connect(self.winc)
                button.enterEvent = lambda event, row=i, col=j: self.highlightBlock(row, col)
                button.leaveEvent = lambda event, row=i, col=j: self.unhighlightBlock(row, col)# Исправленная опечатка в имени функции
                self.gamebox.addWidget(button, i, j)


    def winc(self):
        self.parent().currentClick()
        win_conditions = [
        [0, 1, 2],  # Horizontal lines
        [3, 4, 5],
        [6, 7, 8],
        [2, 5, 8],  # Vertical lines
        [0, 3, 6],
        [1, 4, 7],
        [0, 4, 8],  # Diagonals
        [2, 4, 6]
        ]


        for condition in win_conditions:
            if all(self.buttons[i].text() == "X" for i in condition):
                self.draw=0
                self.Win="X"
                self.enabled = True
                self.disableButtons()
                self.createWinButton()
                self.parent().CheckOnSmallWin()
                break


        for condition in win_conditions:
            if all(self.buttons[i].text() =="0" for i in condition):
                self.draw=0
                self.Win="0"
                self.disableButtons()
                self.createWinButton()
                self.parent().CheckOnSmallWin()
                break
        if all(not button.isEnabled() for button in self.buttons) and self.draw == 1:
            print("DRAW")
            self.NeedToSayAbDraw=1


    def disableButtons(self):
        for button in self.buttons:
            button.setEnabled(False)
            button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")


    def setTextStyleFor1But(self,button):
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        button.setFont(font)


    def createWinButton(self):
        self.WinButton = QPushButton(self.Win)
        self.WinButton.setFixedSize(155, 155)
        self.WinButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setbutEnabled(False)
        self.hideAll()
        self.setTextStyleFor1But(self.WinButton)
        self.WinButton.setEnabled(False)
        self.gamebox.addWidget(self.WinButton, 0, 0, 3, 3)


    def setbutEnabled(self, enabled):
        for button in self.buttons:
            if button.text() == "":
                button.setEnabled(enabled)


    def setbutStyle(self, visibility):
        for button in self.buttons:
            if button.text() == "":
                button.setStyleSheet("background-color: rgba(255, 255, 0, %s);" % visibility)


    def highlightBlock(self, row, col):
        button_index = row * 3 + col
        button = self.buttons[button_index]
        self.previousStyle = button.styleSheet()
        button.setStyleSheet("background-color: rgba(255, 255, 0, 0.5);")


    def unhighlightBlock(self, row, col):
        button_index = row * 3 + col
        button = self.buttons[button_index]
        if button.text()!="":
            button.setStyleSheet("background-color: rgba(255, 255, 0, 0);")
        else:
            button.setStyleSheet(self.previousStyle)


    def setInvisibleTextStyleFor1But(self,button):
        button.setStyleSheet("color: transparent;")
    def hideAll(self):
        for button in self.buttons:
            if button.text() == "":
                button.hide()
