from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer,QUrl
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWebEngineWidgets import *
from PIL import Image
from PIL.ImageQt import ImageQt
import sys, os, json

class apx(QtWidgets.QMainWindow):
    def __init__(self):
        super(apx, self).__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = apx()
    window.show()
    app.exec_()