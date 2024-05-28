from PyQt6.QtWidgets import QFileDialog, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt6.QtGui import QPixmap

class Opponents(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.name_label = QLabel("Player: ")
        self.name_input = QLineEdit()
        self.NameRemoveButton = QPushButton("Remove Name")
        self.picture = QLabel()
        self.file_name=""
        self.image_path=""
        self.input_field = QLineEdit()
        self.pixmap = QPixmap()
        self.Open_button = QPushButton("Open")
        self.Remove_button = QPushButton("Remove")
        self.picture.setPixmap(self.pixmap)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.NameRemoveButton)

        self.layout.addWidget(self.picture)

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.Open_button)
        self.layout.addWidget(self.Remove_button)


        self.input_field.editingFinished.connect(self.openImage)
        self.Open_button.clicked.connect(self.showImage)
        self.name_input.textChanged.connect(self.updateNameLabel)
        self.name_input.returnPressed.connect(self.lockNameLabel)
        self.NameRemoveButton.clicked.connect(self.removeName)
        self.Remove_button.clicked.connect(self.removePict)

        self.setFixedSize(400, 350)

    def openImage(self):
            self.image_path = self.input_field.text()

            if self.image_path:  # Checking that the path to the image is not empty
                pixmap = QPixmap(self.image_path)

                if not pixmap.isNull():  # Checking that pixmap is valid
                    self.pixmap = pixmap.scaled(400, 300)
                    self.picture.setPixmap(self.pixmap)
                else:
                    print("Неверный файл изображения:", self.image_path)
            else:
                print("Не указан путь к файлу изображения.")


    def showImage(self):
        file_dialog = QFileDialog()
        self.file_name, _ = file_dialog.getOpenFileName()
        if self.file_name:  # Checking that a file has been selected
            self.pixmap = QPixmap(self.file_name)
            self.pixmap = self.pixmap.scaled(400, 300)
            self.picture.setPixmap(self.pixmap)

    def updateNameLabel(self):
            name = self.name_input.text()
            self.name_label.setText("Player: " + name)

    def getName(self):
        return self.name_input.text()

    def lockNameLabel(self):

        self.name_input.setReadOnly(True)

    def removeName(self):
        self.name_input.clear()
        self.name_input.setReadOnly(False)

    def removePict(self):
        self.picture.clear()

    def setImage(self, image_path):
        self.file_name = image_path
        self.pixmap = QPixmap(self.file_name)
        self.pixmap = self.pixmap.scaled(400, 300)
        self.picture.setPixmap(self.pixmap)
