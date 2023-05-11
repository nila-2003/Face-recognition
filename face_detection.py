# -*- coding: utf-8 -*-
"""Face detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Oy6PuQCxOvoLyyOBNWjent0Ou-AylMc
"""

!pip install opencv-python

import cv2
face_cascade= cv2.CascadeClassifier("C:\Face-detection\haarcascade_frontalface_default.xml")
cap= cv2.VideoCapture(0) #from webcam
while True:
  _, img= cap.read() #flag and frame
  gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces= face_cascade.detectMultiScale(gray, 1.1, 4)
  for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
  cv2.imshow('img',img)

  k=cv2.waitKey(30) & 0xff
  if k==27:
    break
cap.release()