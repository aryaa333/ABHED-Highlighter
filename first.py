from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFile.setGeometry(QtCore.QRect(60, 180, 401, 31))
        self.pushButtonFile.setObjectName("pushButtonFile")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(70, 30, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setObjectName("heading")
        self.pushButtonURL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonURL.setGeometry(QtCore.QRect(60, 250, 401, 31))
        self.pushButtonURL.setObjectName("pushButtonURL")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sample"))
        self.pushButtonFile.setText(_translate("MainWindow", "UPLOAD  FILE"))
        self.heading.setText(_translate("MainWindow", "ABHED  HIGHLIGHTER"))
        self.pushButtonURL.setText(_translate("MainWindow", "UPLOAD  URL"))