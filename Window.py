# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowSecond(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textbox = QtWidgets.QLabel(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(280, 10, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Rosewood Std Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.textbox.setFont(font)
        self.textbox.setObjectName("textbox")
        self.pushButtonUploadfile1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUploadfile1.setGeometry(QtCore.QRect(120, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUploadfile1.setFont(font)
        self.pushButtonUploadfile1.setObjectName("pushButtonUploadfile1")
        self.pushButtonUploadfile2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonUploadfile2.setGeometry(QtCore.QRect(580, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUploadfile2.setFont(font)
        self.pushButtonUploadfile2.setObjectName("pushButtonUploadfile2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 520, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(324, 80, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 120, 321, 391))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(440, 120, 341, 391))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textbox.setText(_translate("MainWindow", "ABHED HIGHLIGHTER"))
        self.pushButtonUploadfile1.setText(_translate("MainWindow", "UPLOAD FILE"))
        self.pushButtonUploadfile2.setText(_translate("MainWindow", "UPLOAD FILE"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "CLICK HERE TO COMPARE"))