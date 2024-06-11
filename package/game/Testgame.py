from PyQt6.QtWidgets import  QWidget,QPushButton, QGridLayout, QLabel,QColorDialog,QMessageBox
from PyQt6.QtGui import  QColor
from PyQt6.QtCore import Qt
from .gameblock import GameBlock


class TestGame(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.parent = parent
        self.FieldBox = QGridLayout(self)
        self.FieldBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FieldBox.setSpacing(0)
        self.FieldBox.setContentsMargins(0, 0, 8, 28)
        self.current= "0"
        self.FieldsWin = [None] * 9
        self.createGameBlocks()#№1
        self.button_index=0

    def disableALLButtons(self):
         for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                block.disableButtons()

    def currentClick(self):
        self.setTextOnLabel()
        clicked_button = self.sender()
        if self.current == "0":
            self.current = "X"
        else: self.current = "0"
        clicked_button.setText(self.current)
        clicked_button.setEnabled(False)

        # Defining the button index
        button_index = None
        for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                if clicked_button in block.buttons:
                    button_index = block.buttons.index(clicked_button)
                    break
            if button_index is not None:
                self.parent.canvas.draw_symbol(i*3+j,button_index//3,button_index%3 , self.current)
                break

    def Winner (self):


        win_conditions = [
        [0, 1, 2],  # Horizontal lines
        [3, 4, 5],
        [6, 7, 8],  # Vertical lines
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonals
        [2, 4, 6]
        ]

        for i in range(8):
            if all(self.FieldsWin[j] == "X" for j in win_conditions[i]):
                if i<3:
                    self.parent.canvas.draw_horizontal_line(i)
                if i>2 and i< 6:
                    self.parent.canvas.draw_vertical_line(i)
                    print(i)
                if i== 6:
                    self.parent.canvas.draw_main_diagonal()
                if i == 7:
                    self.parent.canvas.draw_secondary_diagonal()

                self.draw=0
                self.Win="X"
                self.showWinMessage(self.parent.opponent1.name_input.text())
                print("WIN X ")
                self.disableALLButtons()

                break


        for i in range(8):
            if all(self.FieldsWin[j] == "0" for j in win_conditions[i]):
                if i<3:
                    self.parent.canvas.draw_horizontal_line(i)
                if i>2 and i< 6:
                    self.parent.canvas.draw_vertical_line(i-3)
                if i== 6:
                    self.parent.canvas.draw_main_diagonal()
                if i == 7:
                    self.parent.canvas.draw_secondary_diagonal()

                self.draw=0
                self.showWinMessage(self.parent.opponent2.name_input.text())
                self.Win="0"
                self.disableALLButtons()
                print("WIN 0 ")

                break
        for i in range(3):
            for j in range(3):
                if self.blocks[i][j].NeedToSayAbDraw ==1:
                    self.disableALLButtons()
                    self.showDrawMessage()

    def blockButtons(self):
            self.fillFieldsWin()
            for m in range(3):
                for n in range(3):
                    if m == (self.button_index)//3 and n == (self.button_index) % 3:
                        if self.FieldsWin[m*3+n] == None:
                            self.blocks[m][n].setInvisibleTextStyleFor1But(self.blocks[m][n])
                            current_block=1
                            other_blocks=0

                            break
                        else :
                            current_block=0
                            other_blocks=1

                            break

            for m in range(3):
                for n in range(3):
                    if m == (self.button_index)//3 and n == (self.button_index) % 3:

                        self.blocks[m][n].setbutEnabled(current_block)
                        self.blocks[m][n].setbutStyle(current_block)
                    else:
                        self.blocks[m][n].setbutEnabled(other_blocks)
                        self.blocks[m][n].setbutStyle(other_blocks)

                    if self.blocks[m][n].Win!="":
                            self.blocks[m][n].setbutEnabled(False)
                            self.blocks[m][n].setbutStyle(0)
            if self.Winner():
                print("THE END")

    def needableField(self):
        self.findIndexOfBut()
        self.blockButtons()

    def createCurrentPlayerLabel(self):
        self.label = QLabel()
        self.FieldBox.addWidget(self.label, 3, 0, 1, 3)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    def setTextOnLabel(self):
        x, y = self.parent.getNameOfPlayer()
        if  self.current == "0":
            self.label.setText("O'S turn:  "+y)
        else :
            self.label.setText("X'S turn:  "+x)

    def createGameBlocks(self):
        self.blocks = [[GameBlock(self) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.blocks[i][j].setStyleSheet("color: transparent;")


        for i in range(3):
            for j in range(3):
                self.FieldBox.addWidget(self.blocks[i][j], i, j)

        for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                for button in block.buttons:
                    button.clicked.connect(self.needableField)#№2
        self.createCurrentPlayerLabel()


    def CheckOnSmallWin(self):
        for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                if block.Win !="" and block.BigSymbolDraw == 0:
                    block.BigSymbolDraw = 1
                    self.parent.canvas.draw_block_symbol(i*3+j,block.Win)


    def findIndexOfBut(self):
        clicked_button = self.sender()
        self.button_index = None
        for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                if block.isAncestorOf(clicked_button):
                    # The index of the button that was pressed was found
                    self.button_index = block.buttons.index(clicked_button)

    def showWinMessage(self, winner):
        QMessageBox.information(self, "Game Over", f"Congratulations, {winner} has won the game!")
        self.parent.canvas.clear()
        self.parent.blocksClear()

    def showDrawMessage(self):
        QMessageBox.information(self, "Game Over", f"Sorry,but DRAWBLOCKS are unavailable in beta-test")
        self.parent.canvas.clear()
        self.parent.blocksClear()

    def fillFieldsWin(self):
         for i in range(3):
            for j in range(3):
                block = self.blocks[i][j]
                if block.Win !="":
                    index = i*3+j
                    self.FieldsWin[index]=block.Win
