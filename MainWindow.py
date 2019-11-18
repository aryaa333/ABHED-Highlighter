from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from first import Ui_MainWindow
from WindowUI import Ui_MainWindow
import sys
import convertapi
from sentence import Sentence
import urllib.request


class MainApp:
    convertapi.api_secret = 'pktrevhuuFmDvpxB'
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        # self.sec = None

    def start(self):
        self.ui.setupUi(self.MainWindow)
        self.init_events1()
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    # def init_events(self):
    #     self.ui.pushButtonFile.clicked.connect(self.button_click)
    #     #self.ui.pushButtonURL.clicked.connect(self.button_click1)

    def init_events1(self):
        self.ui.pushButtonUploadfile1.clicked.connect(self.uploadFile1)
        self.ui.pushButtonUploadUrl.clicked.connect(self.uploadURL1)
        self.ui.pushButtonUploadUrl2.clicked.connect(self.uploadURL2)
        self.ui.pushButtonUploadfile2.clicked.connect(self.uploadFile2)
        self.ui.pushButton_3.clicked.connect(self.compare)
        self.ui.pushButtonClear.clicked.connect(self.clear)

    def uploadURL1(self):
        self.path = self.ui.lineEditPath.text()


        try:
            self.result = convertapi.convert('txt', {'File': self.path})
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text1.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
            self.ss1=f1.read()
        except:
            self.data = urllib.request.urlopen(self.path).read()  # it's a file like object and works just like a file
            self.ss1 = str(self.data)
        self.ui.listWidget.addItem(self.ss1)

    def uploadURL2(self):
        self.path = self.ui.lineEditPath2.text()

        try:
            self.result = convertapi.convert('txt', {'File': self.path})
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text1.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
            self.ss2 = f1.read()
        except:
            self.data = urllib.request.urlopen(self.path).read()  # it's a file like object and works just like a file
            self.ss2=str(self.data)
        self.ui.listWidget_2.addItem(self.ss2)

    def uploadFile1(self):
        print('PyQt5 button click')
        self.dlg = QFileDialog()
        if self.dlg.exec():
            self.path = self.dlg.selectedFiles()[0]
            print(self.path)
            self.ui.lineEditPath.setText(self.path)
        try:
            self.result = convertapi.convert('txt', {'File': self.path})
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text1.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
        except:
            f1 = open(self.path)
        self.ss1 = f1.read()
        self.ui.listWidget.addItem(self.ss1)
    def uploadFile2(self):
        print('PyQt5 button click')
        self.dlg = QFileDialog()
        if self.dlg.exec():
            self.path = self.dlg.selectedFiles()[0]
            print(self.path)
            self.ui.lineEditPath2.setText(self.path)

        try:
            self.result = convertapi.convert('txt', {'File': self.path})
            self.dest = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\files\text2.txt'
            self.result.file.save(self.dest)
            f1 = open(self.dest, encoding="utf8")
        except:
            f1 = open(self.path)
        self.ss2 = f1.read()
        self.ui.listWidget_2.addItem(str(self.ss2))
        # removeItemWidget

    def button_click(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow1 = QtWidgets.QMainWindow()
        self.sec = Ui_MainWindow()
        self.sec.setupUi(self.MainWindow1)
        self.init_events1()
        self.MainWindow1.show()
        # self.sec.show()

    def clear(self):

        # self.curItem = self.ui.listWidget.currentItem()
        # self.ui.listWidget.removeItemWidget(self.curItem)
        self.item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
        self.item = None
        self.item1 = self.ui.listWidget_2.takeItem(self.ui.listWidget_2.currentRow())
        self.item1 = None

        self.ui.listWidget.setStyleSheet("color:black")
        self.ui.listWidget_2.setStyleSheet("color:black")
    def compare(self):
        se = Sentence()
        se.cosine_distance_wordembedding_method(self.ss1,self.ss2, self.ui.listWidget,self.ui.listWidget_2)

if __name__ == "__main__":
    main_app = MainApp()
    main_app.start()
