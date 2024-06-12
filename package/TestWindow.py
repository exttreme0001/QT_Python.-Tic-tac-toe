from PyQt6.QtWidgets import QMainWindow, QHBoxLayout,QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QPainter
from jsonsave.save import JsonSave
from menu import TestMenu
from Opponent import Opponents
from game import TestGame
from game import canva
import os
import json

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0,1920, 1080)
        self.createCentralWidget()
        self.createPlayer1()
        self.createCanvas()
        self.createMenuBar()
        self.createField()
        self.createPlayer2()
        self.setCentralWidget(self.central_widget)
        self.json_save = JsonSave()


    def createCentralWidget(self):

        self.central_widget = QWidget()
        #self.central_widget_label = QLabel("Default text")
        #self.central_widget_label.setAlignment(
          #  Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.layout = QHBoxLayout(self.central_widget)
       # self.layout.addWidget(self.central_widget_label)

    def createField(self):
        self.field=TestGame(self)
        self.field.setGeometry(500,155,500,500)

        self.layout.addWidget(self.field)

    def createPlayer1(self):
        self.opponent1 = Opponents(self.central_widget)
        self.layout.addWidget(self.opponent1)
        self.opponent1.move(0,200)

    def createPlayer2(self):
        self.opponent2 = Opponents(self.central_widget)
        self.layout.addWidget(self.opponent2)
        self.opponent2.move(1100,200)
    def createCanvas(self):
        self.canvas = canva.Canvas_Block(self)
        self.canvas.setGeometry(509,150,520,520)
        self.canvalayout = QVBoxLayout()
        self.canvalayout.addWidget(self.canvas)

    def getNameOfPlayer(self):
        x=self.opponent1.name_input.text()
        y=self.opponent2.name_input.text()
        return x,y
    def createMenuBar(self):
        self.menuBar = TestMenu(self)
        self.menuBar.addLoadActionHandler(self.load_data)
        self.menuBar.addSaveActionHandler(self.save_data)
        self.menuBar.addOpenFileActionHandler(self.openFile)
        self.setMenuBar(self.menuBar)

    def save_data(self):
        self.image = self.canvas.grab().toImage()
        imgp='C:/Users/egori/OneDrive/Рабочий стол/pepe.png'
        image_path = os.path.join(imgp)
        self.image.save(image_path, "PNG")
        opponent_1_name, opponent_2_name = self.getNameOfPlayer()
        self.json_save.save_data(self.canvas.canva_color.name(),self.canvas.x_color.name(),self.canvas.o_color.name(),opponent_1_name, opponent_2_name,self.opponent1.image_path,self.opponent2.image_path ,self.opponent1.file_name,self.opponent2.file_name,image_path,self.field.blocks,self.field.FieldsWin,self.field.button_index)

    def load_data(self):
        try:
            load_path = self.json_save.select_load_path()
            if load_path is not None:
                try:
                    self.json_save.load_data(load_path)
                    self.blocksClear()
                    self.opponent1.name_input.setText(self.json_save.opponent_1_name)
                    self.opponent2.name_input.setText(self.json_save.opponent_2_name)
                    self.canvas_image = QPixmap(self.json_save.canvas_pic_path)
                    if self.json_save.from_path_opp1_pic !="":
                        self.opponent1.setImage(self.json_save.from_path_opp1_pic)
                    else:
                        self.opponent1.setImage(self.json_save.pict_opp_1)
                    if self.json_save.from_path_opp2_pic !="":
                        self.opponent2.setImage(self.json_save.from_path_opp2_pic)
                    else:
                        self.opponent2.setImage(self.json_save.pict_opp_2)
                    self.canvas.x_color.setNamedColor(self.json_save.x_color)
                    self.canvas.o_color.setNamedColor(self.json_save.o_color)
                    self.canvas.canva_color.setNamedColor(self.json_save.field_color)
                    self.canvas.update_canvas_image(self.canvas_image)
                    self.field.FieldsWin=self.json_save.FieldsWin
                    self.setTextOnBut()
                    self.field.button_index=self.json_save.buttonIndex
                    self.field.blockButtons()
                    self.display_canvas_image()
                except FileNotFoundError:
                    print("FileNotFound")
                except json.JSONDecodeError:
                    print("JSONDecodeError.")
                except Exception as e:
                    print(f"Exception: {e}")
            else:
                print("canceled")
                return

        except FileNotFoundError:
                    pass
    def display_canvas_image(self):
        if self.canvas_image and not self.canvas_image.isNull():
            painter = QPainter(self.canvas)
            painter.drawPixmap(0, 0, self.canvas_image)
            painter.end()

    def openFile(self):
        self.central_widget_label.setText("Open file action triggered")
    def getNameOfOpp1(self):
        name=self.opponent1.name_input
        return name
    def getNameOfOpp2(self):
        name=self.opponent2.name_input
        return name
    def setTextOnBut(self):# processing of all buttons including win
        for i in range(len(self.field.blocks)):
            for j in range(len(self.field.blocks[i])):
                for k in range(len(self.field.blocks[i][j].buttons)):
                    buttonI_value = getattr(self.json_save, f"gameblock{i*3 + j + 1}")[k]
                    self.field.blocks[i][j].buttons[k].setText(buttonI_value)
                    self.field.blocks[i][j].setInvisibleTextStyleFor1But(self.field.blocks[i][j])
                    if self.field.blocks[i][j].buttons[k].text() != "":
                        self.field.blocks[i][j].buttons[k].setEnabled(False)
                if  self.field.FieldsWin[i*3+j] != None:
                    self.field.blocks[i][j].disableButtons()
                    self.field.blocks[i][j].createWinButton()
    def blocksClear(self):

        self.opponent1.deleteLater()
        self.opponent2.deleteLater()
        self.createPlayer1()
        self.newField=TestGame(self)
        self.newField.setGeometry(500,155,500,500)
        self.field.deleteLater()
        self.field = self.newField
        self.layout.addWidget(self.field)
        self.createPlayer2()
