import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.title = "MyNote"

        self.top= 150

        self.left= 150

        self.width = 500

        self.height = 500

        self.InitWindow()

    def InitWindow(self):

        self.setWindowTitle(self.title)

        self.setGeometry(self.top, self.left, self.width, self.height)

        self.show()

App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())