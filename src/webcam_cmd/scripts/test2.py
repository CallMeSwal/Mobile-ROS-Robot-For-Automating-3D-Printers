import cv2 
import numpy as np 
import time
  
# taking the input from webcam 
# running while loop just to make sure that 
# our program keep running untill we stop it 
cams_test = 500
for i in range(0, cams_test):
    print("Hi",  i)
    cap = cv2.VideoCapture(i)
    test, frame = cap.read()
    if test:
        print("i : "+str(i)+" /// result: "+str(test))
