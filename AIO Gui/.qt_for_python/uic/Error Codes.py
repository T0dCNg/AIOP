# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ogban\Desktop\The-All-In-One-Project\The-All-In-One-Project\AIO Gui\Error Codes.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 530)
        Dialog.setMinimumSize(QtCore.QSize(491, 530))
        Dialog.setMaximumSize(QtCore.QSize(491, 530))
        Dialog.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 510, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(42)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(230, 200, 85);")
        self.label.setObjectName("label")
        self.Close = QtWidgets.QPushButton(Dialog)
        self.Close.setGeometry(QtCore.QRect(0, 470, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Close.setFont(font)
        self.Close.setStyleSheet("background-color: rgb(213, 0, 0);")
        self.Close.setAutoDefault(False)
        self.Close.setDefault(False)
        self.Close.setObjectName("Close")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 120, 491, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("border-color: rgb(55, 255, 0);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 472, 491))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 491))
        self.scrollAreaWidgetContents.setStyleSheet("QScrollBavertical{\n"
"    \n"
"    color: rgb(230, 200, 85);\n"
"    background-color: rgb(40, 41, 35);\n"
"}")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_2.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_3.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_4.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(230, 200, 85);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 100, 491, 20))
        self.line.setMaximumSize(QtCore.QSize(491, 150))
        self.line.setStyleSheet("background-color: rgb(40, 41, 35);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AIO | Error Codes"))
        self.label_3.setText(_translate("Dialog", "AIO \"GUI Edittion\" | Version: v-2.1.1 REV-3 | GUI Version:Alpha 0.0.4 | Copyright AIO 2022"))
        self.label.setText(_translate("Dialog", "AIO Error Codes"))
        self.Close.setText(_translate("Dialog", "Close"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Blank</p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Error Code 3: Invalid Input</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Error Code 1: Invalid Option.Chose</p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Error Code 2: Incorect Username Or Password</p></body></html>"))