from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title
        self.setWindowTitle('Paint App')
        # set window geometry
        self.setGeometry(350, 150, 600, 500)

        # creating image on window
        self.image = QImage(self.size(), QImage.Format_RGB32)
        # fill white color to image
        self.image.fill(Qt.white)
        # set draw to false
        self.draw = False
        # set brush size
        self.brushSize = 2
        # set brush color
        self.brushColor = Qt.black
        # create QPoint instance to trace the point
        self.lastPoint = QPoint()
        # create menu bar
        mainMenu = self.menuBar()
        # create file menu
        fileMenu = mainMenu.addMenu('File')
        saveAction = QAction('Save', self)
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)
        clearAction = QAction('Clear', self)
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        # create size menu
        size = mainMenu.addMenu('Brush Size')
        size_2 = QAction('2px', self)
        size.addAction(size_2)
        size_2.triggered.connect(self.size_2)
        size_4 = QAction('4px', self)
        size.addAction(size_4)
        size_4.triggered.connect(self.size_4)
        size_6 = QAction('6px', self)
        size.addAction(size_6)
        size_6.triggered.connect(self.size_6)
        size_8 = QAction('8px', self)
        size.addAction(size_8)
        size_8.triggered.connect(self.size_8)
        size_10 = QAction('10px', self)
        size.addAction(size_10)
        size_10.triggered.connect(self.size_10)
        # create color menu
        color = mainMenu.addMenu('Brush Color')
        black = QAction('Black', self)
        color.addAction(black)
        black.triggered.connect(self.blackColor)
        red = QAction('Red', self)
        color.addAction(red)
        red.triggered.connect(self.redColor)
        blue = QAction('Blue', self)
        color.addAction(blue)
        blue.triggered.connect(self.blueColor)
        green = QAction('Green', self)
        color.addAction(green)
        green.triggered.connect(self.greenColor)
        yellow = QAction('Yellow', self)
        color.addAction(yellow)
        yellow.triggered.connect(self.yellowColor)

    def mousePressEvent(self, event):
        # check if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # set draw to true
            self.draw = True
            # set position of last point
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        # check if left button is pressed
        # and draw flag is true
        if Qt.LeftButton & self.draw:
            # create painter instance with image
            painter = QPainter(self.image)

            # set the pen or brush of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            # draw line from the last positioned point of cursor
            # to the current position point
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point with current point
            self.lastPoint = event.pos()
            # update window
            self.update()

    def mouseReleaseEvent(self, event):
        # check if left mouse button is kept
        # pressed while drawing
        if event.button() == Qt.LeftButton:
            # if the button click is released
            # then set draw to false
            self.draw = False

    def paintEvent(self, event):
        # create a painter canvas
        canvasPainter = QPainter(self)

        # draw image rectangle on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        savePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;All Files(*.*) ")
        if savePath == "":
            return None
        self.image.save(savePath)

    def clear(self):
        # clear drawing from canvas image
        self.image.fill(Qt.white)
        # update window
        self.update()

    # methods to change brush size
    def size_2(self):
        self.brushSize = 2

    def size_4(self):
        self.brushSize = 4

    def size_6(self):
        self.brushSize = 6

    def size_8(self):
        self.brushSize = 8

    def size_10(self):
        self.brushSize = 10

    # methods to change brush color
    def blackColor(self):
        self.brushColor = Qt.black

    def redColor(self):
        self.brushColor = Qt.red

    def blueColor(self):
        self.brushColor = Qt.blue

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


# create pyqt5 app
App = QApplication(sys.argv)
# create window instance
window = Window()
# display window
window.show()
# start the app
sys.exit(App.exec())