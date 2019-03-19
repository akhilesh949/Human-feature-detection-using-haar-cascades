# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:28:29 2019

@author: Akhilesh
"""


import numpy as np
import cv2


cap = cv2.VideoCapture('friends.mkv')
#length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))





fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter('Person.mp4',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)



    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ ew, ey+eh), (0, 255,0), 2)
    
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, 'Person Detected', (200,200), font , 1, (230, 120, 120), 2, cv2.LINE_AA)
        
    
    cv2.imshow('frame', frame)
        
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

cap.release()
cv2.destroyAllWindows()    
