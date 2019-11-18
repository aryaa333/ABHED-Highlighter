import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
import convertapi
from sentence import Sentence


class App(QWidget):
    convertapi.api_secret = 'MUNDJLAsbd3MisR6'

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton('File1', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        button.clicked.connect(self.on_click)
        button1 = QPushButton('File2', self)
        button1.setToolTip('This is an example button')
        button1.move(200, 70)
        button1.clicked.connect(self.on_click1)
        button2 = QPushButton('Process', self)
        button2.setToolTip('This is an example button')
        button2.move(150, 140)
        button2.clicked.connect(self.process)
        self.show()

    def on_click(self):
        print('PyQt5 button click')
        self.dlg= QFileDialog()
        if self.dlg.exec():
            self.path = self.dlg.selectedFiles()[0]
            print(self.path)
        try:
            self.result = convertapi.convert('txt', {'File': self.path })
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text1.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
        except:
            f1 = open(self.path)

        self.ss1 = f1.read()
        print(self.ss1)
    def on_click1(self):
        print('PyQt5 button1 click')
        self.dlg = QFileDialog()
        if self.dlg.exec():
            self.path = self.dlg.selectedFiles()[0]
            print(self.path)
        try:
            self.result = convertapi.convert('txt', {'File': self.path})
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text2.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
        except:
            f1 = open(self.path)

        self.ss2 = f1.read()

    def process(self):
        se = Sentence()
        se.cosine_distance_wordembedding_method(self.ss1,self.ss2)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


