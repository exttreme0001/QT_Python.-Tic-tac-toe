
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPainter, QPen, QBrush,QPixmap
from PyQt6.QtWidgets import  QLabel,QWidget
from PyQt6.QtWidgets import QWidget
class Canvas_Block(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.label = QLabel()
        self.canvas = QPixmap(520, 520)
        self.canvas_image = None
        self.canvas.fill(QColor("black"))
        self.label.setGeometry(0, 0, self.canvas.width(), self.canvas.height())
        self.draw_border()
        self.draw_lines()
        self.draw_little_lines()
        if self.canvas_image:
            self.label.setPixmap(self.canvas_image)
        else:
            self.label.setPixmap(self.canvas)


    def update_canvas_image(self, new_image):
        self.canvas_image = new_image.scaled(self.label.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        self.update()
        self.label.setPixmap(self.canvas_image)

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.canvas_image:
            painter.drawPixmap(0, 0, self.canvas_image)
        else:
            painter.drawPixmap(0, 0, self.canvas)

    def draw_border(self):
        if self.canvas_image:
            painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor("black"))
        painter.setPen(pen)
        brush = QBrush(QColor("#376F9F"))
        painter.setBrush(brush)


        painter.drawRect(0,0,520,520)
        self.update()

    def draw_lines(self):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(9)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

       # Drawing horizontal lines
        painter.drawLine(0, self.canvas.height() // 3, self.canvas.width(), self.canvas.height() // 3)
        painter.drawLine(0, (self.canvas.height() // 3) * 2, self.canvas.width(), (self.canvas.height() // 3) * 2)

        # Drawing vertical lines
        painter.drawLine(self.canvas.width() // 3, 0, self.canvas.width() // 3, self.canvas.height())
        painter.drawLine((self.canvas.width() // 3) * 2, 0, (self.canvas.width() // 3) * 2, self.canvas.height())
        self.update()

    def draw_little_lines(self):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(4)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

       # Drawing horizontal lines
        painter.drawLine(0, self.canvas.height() // 9, self.canvas.width(), self.canvas.height() // 9)
        painter.drawLine(0, (self.canvas.height() // 9) * 2, self.canvas.width(), (self.canvas.height() // 9) * 2)

        painter.drawLine(0, (self.canvas.height() // 9) * 4+4, self.canvas.width(), (self.canvas.height() // 9) * 4+4)
        painter.drawLine(0, (self.canvas.height() // 9)* 5, self.canvas.width(), (self.canvas.height() // 9)*5)

        painter.drawLine(0, (self.canvas.height() // 9) *7+4, self.canvas.width(), (self.canvas.height() // 9)*7+4)
        painter.drawLine(0, (self.canvas.height() // 9) * 8, self.canvas.width(), (self.canvas.height() // 9) * 8)

        # Drawing vertical lines
        painter.drawLine(self.canvas.width() // 9, 0, self.canvas.width() // 9, self.canvas.height())
        painter.drawLine((self.canvas.width() // 9) * 2, 0, (self.canvas.width() // 9) * 2, self.canvas.height())

        painter.drawLine((self.canvas.width() // 9)*4, 0,(self.canvas.width() // 9)*4, self.canvas.height())
        painter.drawLine((self.canvas.width() // 9) * 5, 0, (self.canvas.width() // 9) * 5, self.canvas.height())

        painter.drawLine((self.canvas.width() // 9)*7+4, 0, (self.canvas.width() // 9)*7+4, self.canvas.height())
        painter.drawLine((self.canvas.width() // 9) * 8, 0, (self.canvas.width() // 9) * 8, self.canvas.height())
        self.update()



    def draw_symbol(self, block_index: int, row_in_block: int, col_in_block: int, symbol: str):
        if self.canvas_image:
            painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(4)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Setting up the brush
        brush = QBrush(QColor("#376F9F"))
        painter.setBrush(brush)

        # Calculating the coordinates of the center of the cell inside the block
        cell_width = self.canvas.width() // 9
        cell_height = self.canvas.height() // 9
        block_width = cell_width * 3
        block_height = cell_height * 3
        center_x = int((block_index % 3) * block_width + (col_in_block + 0.5) * cell_width)
        center_y = int((block_index // 3) * block_height + (row_in_block + 0.5) * cell_height)

        # Character rendering depending on the passed parameter
        if symbol == "X":
            painter.drawLine(center_x - cell_width // 4, center_y - cell_height // 4,
                            center_x + cell_width // 4, center_y + cell_height // 4)
            painter.drawLine(center_x - cell_width // 4, center_y + cell_height // 4,
                            center_x + cell_width // 4, center_y - cell_height // 4)
        elif symbol == "0":
            painter.drawEllipse(center_x - cell_width // 4, center_y - cell_height // 4,
                                cell_width // 2, cell_height // 2)
        self.update()

    def draw_block_symbol(self, block_index: int, symbol: str):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(10)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Setting up the brush
        brush = QBrush(QColor("#376F9F"))
        painter.setBrush(brush)

        # Calculating block coordinates
        cell_width = self.canvas.width() // 9
        cell_height = self.canvas.height() // 9
        block_width = cell_width * 3
        block_height = cell_height * 3
        block_x = (block_index % 3) * block_width
        block_y = (block_index // 3) * block_height

        # Character rendering depending on the passed parameter
        if symbol == "X":
            # Drawing a cross on a block
            painter.drawLine(block_x, block_y, block_x + block_width, block_y + block_height)
            painter.drawLine(block_x + block_width, block_y, block_x, block_y + block_height)
        elif symbol == "0":
            # Drawing a circle on a block
            painter.drawEllipse(block_x+11, block_y+12, block_width-20, block_height-20)
        self.update()

    def draw_horizontal_line(self, row: int):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Настройка пера
        pen = QPen()
        pen.setWidth(16)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Вычисление координат горизонтальной линии
        cell_height = self.canvas.height() // 9
        line_y = (row * 3 + 1) * cell_height
        painter.drawLine(0, line_y+33, self.canvas.width(), line_y+33)
        self.update()

    def draw_vertical_line(self, col: int):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(13)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Calculating the coordinates of a vertical line
        cell_width = self.canvas.width() // 9
        line_x = (col * 3 + 1) * cell_width
        painter.drawLine(line_x+33, 0, line_x+33, self.canvas.height())
        self.update()

    def draw_main_diagonal(self):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(8)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Drawing the main diagonal
        painter.drawLine(0, 0, self.canvas.width(), self.canvas.height())
        self.update()

    def draw_secondary_diagonal(self):
        if self.canvas_image:
         painter = QPainter(self.canvas_image)
        else:
            painter=QPainter(self.canvas)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Setting up the pen
        pen = QPen()
        pen.setWidth(8)
        pen.setColor(QColor("black"))
        painter.setPen(pen)

        # Drawing a side diagonal
        painter.drawLine(0, self.canvas.height(), self.canvas.width(), 0)
        self.update()
    def clear(self):
        self.canvas.fill(QColor("black"))
        self.draw_border()
        self.draw_lines()
        self.draw_little_lines()
        self.label.setPixmap(self.canvas)
