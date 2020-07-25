# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xinxi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 602)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 520, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.cameraLabel = QtWidgets.QLabel(Form)
        self.cameraLabel.setGeometry(QtCore.QRect(30, 80, 321, 321))
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraButton = QtWidgets.QPushButton(Form)
        self.cameraButton.setGeometry(QtCore.QRect(30, 450, 121, 51))
        self.cameraButton.setObjectName("cameraButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 520, 121, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(230, 450, 121, 51))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "信息录入"))
        self.pushButton.setText(_translate("Form", "返回上一级"))
        self.cameraLabel.setText(_translate("Form", "请依次①打开摄像头②关闭摄像头\n③输入名字④开始录入"))
        self.cameraButton.setText(_translate("Form", "打开摄像头"))
        self.pushButton_3.setText(_translate("Form", "开始录入"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">这里输入你的名字</p></body></html>"))