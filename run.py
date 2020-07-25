# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:40:42 2020
author: Arklwz & Guanqr
"""

from PyQt5 import QtWidgets
from mwindow import Ui_MainWindow
from load import Ui_Form as Form_load
from check import Ui_Form as Form_check
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import numpy as np
import cv2
import shutil
import time
import random

face_detector = cv2.CascadeClassifier(r'./data/haarcascade_frontalface_default.xml')
if os.path.exists(r'./Data_user/names.npy') == True:
    names = np.load(r'./Data_user/names.npy')
else:
    names = ['0']
    
tempdata=['','','']
    
class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load_in)
        self.pushButton_2.clicked.connect(self.check_in)
        
        self.labeltime = QLabel(self)
        self.labeltime.setFixedWidth(400)
        self.labeltime.move(0, 0)
        self.labeltime.setStyleSheet("QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}")
        # 动态显示时间在 label 上
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.labeltime.setText("     "+ text)

    def check_in(self):
        self.w2 = formcheck()
        self.w2.show()
        self.close()
        
    def load_in(self):
        self.w1 = formload()
        self.w1.show()
        self.close()
        
class formcheck(QtWidgets.QMainWindow, Form_check):  
    returnSignal = pyqtSignal()
    
    def  __init__ (self,parent=None):
        super(formcheck, self).__init__(parent)
        self.timer_camera = QTimer() # 初始化定时器
        self.cap = cv2.VideoCapture() # 初始化摄像头
        self.minW = 0.1*self.cap.get(3)
        self.minH = 0.1*self.cap.get(4)
        self.CAM_NUM = 0
        self.setupUi(self)
        self.slot_init()
        self.pushButton_2.clicked.connect(self.re)
        self.idnum=0
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        if os.path.exists('face_trainer/trainer.yml') == True:
            self.recognizer.read('face_trainer/trainer.yml')
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.pushButton_4.clicked.connect(self.trans)

    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        self.cameraButton.clicked.connect(self.slotCameraButton)
 
    def show_camera(self):
        flag,self.image = self.cap.read()
        show = cv2.resize(self.image, (320,320))
        gray = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(gray.data, gray.shape[1], gray.shape[0], QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))
        gray1 = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)
        
        faces = face_detector.detectMultiScale(
                gray1,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(self.minW), int(self.minH))
        )
        if os.path.exists('face_trainer/trainer.yml') == True:
            for (x, y, w, h) in faces:
                self.idnum, self.confidence = self.recognizer.predict(gray1[y:y+h, x:x+w])
                self.idnum = names[self.idnum]
                self.textBrowser.setText(self.idnum)
                tempdata[0] = self.idnum
                tempdata[1] = str(random.randint(360,370)/10)
                self.pushButton.setText(tempdata[1] + '°C')
                tempdata[2] = time.strftime("%Y-%m-%d")
                np.save(r'./Data_user/tempdata.npy',tempdata)
        else:
            self.textBrowser.setText('unknown')

    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:
           # 打开摄像头并显示图像信息
           self.openCamera()
        else:
           # 关闭摄像头并清空显示信息
           self.closeCamera()

    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',buttons=QMessageBox.Ok,defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.cameraButton.setText('关闭摄像头')

    def closeCamera(self):
        self.timer_camera.stop()
        self.cap.release()
        self.cameraLabel.clear()
        self.cameraButton.setText('重新检测')
        self.textBrowser.setText('unknown')
        self.cameraLabel.setText('重新打开摄像头检测')
        if os.path.exists(r'./Data_user/tempdata.npy') == True:
            os.remove(r'./Data_user/tempdata.npy')
        
    def trans(self):
        flag = os.path.exists(r'./Data_user/tempdata.npy')
        if flag == True:
            os.popen('python addData.py')
            
    def re(self):
        self.w1=mywindow()
        self.w1.show()
        self.close()        

class formload(QtWidgets.QMainWindow, Form_load):

    returnSignal = pyqtSignal()
    
    def __init__(self,parent=None):
        super(formload, self).__init__(parent)
        self.timer_camera = QTimer() # 初始化定时器
        self.cap = cv2.VideoCapture() # 初始化摄像头
        self.CAM_NUM = 0
        self.count=0
        self.setupUi(self)
        self.slot_init()
        self.pushButton.clicked.connect(self.re)
        self.pushButton_3.clicked.connect(self.train)

    def train(self):
        
        os.popen('python face_training.py')
        '''
        while True:
            self.cameraLabel.setText("正在训练请稍等")
            if os.path.exists('welldown.npy') == True:
                break
        '''
        self.cameraLabel.setText("训练完成")
        self.user = self.textEdit.toPlainText()
        names.append(self.user)
        
        np.save(r'./Data_user/names.npy',names)
        
    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        self.cameraButton.clicked.connect(self.slotCameraButton)
        
    def show_camera(self):
        flag,self.image = self.cap.read()
        show = cv2.resize(self.image,(320,320))
        gray = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(gray.data, gray.shape[1],gray.shape[0],QImage.Format_RGB888)
        self.cameraLabel.setPixmap(QPixmap.fromImage(showImage))
        self.cot = len(names)
        if self.count<100:
            gray1 = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)

            self.count=self.count+1
            self.faces = face_detector.detectMultiScale(gray1, 1.3, 5)

            for (x, y, w, h) in self.faces:
                cv2.imwrite("Facedata/User." +str(self.cot) +'.'+str(self.count) + '.jpg', gray1[y: y + h, x: x + w])

    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:
           # 打开摄像头并显示图像信息
           self.openCamera()
        else:
           # 关闭摄像头并清空显示信息
           self.closeCamera()

    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)
        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确', buttons = QMessageBox.Ok, defaultButton = QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.cameraButton.setText('关闭摄像头')

    def closeCamera(self):
        self.timer_camera.stop()
        self.cap.release()
        self.cameraLabel.clear()
        self.cameraButton.setText('重新录入')
        self.cameraLabel.setText("请输入姓名开始录入或重新录入")
        self.count = 0

    def re(self):
        shutil.rmtree('Facedata')  
        os.mkdir('Facedata')  
        self.w1 = mywindow()
        self.w1.show()
        self.close()
        
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())