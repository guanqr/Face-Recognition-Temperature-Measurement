import numpy as np
from PIL import Image
import os
import cv2

# 人脸数据路径
path = 'Facedata'
if os.path.exists(r'./Data_user/faces.npy') == True:
    oldfaces = np.load(r'./Data_user/faces.npy',allow_pickle=True)
    oldids = np.load(r'./Data_user/ids.npy')
    
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(r'./data/haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # join函数的作用？
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')   # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x: x + w])
            ids.append(id)
    return faceSamples, ids

faces, ids = getImagesAndLabels(path)

if os.path.exists(r'./Data_user/faces.npy') == True:
    newfaces=np.hstack((oldfaces,faces))
    newids = np.hstack((oldids,ids))
    np.save(r'./Data_user/faces.npy',newfaces)
    np.save(r'./Data_user/ids.npy',newids)
    recognizer.train(newfaces, np.array(newids))
else:
    recognizer.train(faces, np.array(ids))
    np.save(r'./Data_user/faces.npy',faces)
    np.save(r'./Data_user/ids.npy',ids)

recognizer.write(r'./face_trainer/trainer.yml')