# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 600)
        self.cameraLabel = QtWidgets.QLabel(Form)
        self.cameraLabel.setGeometry(QtCore.QRect(20, 70, 321, 321))
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraButton = QtWidgets.QPushButton(Form)
        self.cameraButton.setGeometry(QtCore.QRect(10, 410, 121, 51))
        self.cameraButton.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 490, 121, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 470, 93, 61))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 470, 121, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 410, 121, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 540, 121, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "红外测温"))
        self.cameraLabel.setText(_translate("Form", "开始检测，确认信息后确认签到"))
        self.cameraButton.setText(_translate("Form", "开始检测"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>:你的温度为</p></body></html>"))
        self.pushButton.setText(_translate("Form", "未测"))
        self.pushButton_4.setText(_translate("Form", "确认签到"))
        self.pushButton_2.setText(_translate("Form", "返回上一级"))