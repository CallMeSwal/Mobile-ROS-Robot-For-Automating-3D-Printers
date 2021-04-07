import cv2 
import numpy as np 
import time
  
# taking the input from webcam 
vid = cv2.VideoCapture(2) 
  
# running while loop just to make sure that 
# our program keep running untill we stop it 

print("hi1")
if vid.read() == False:
    print("hi2")
    vid.open()


while True:
  
    # capturing the current frame 
    _, frame = vid.read() 
  
    # displaying the current frame 
    # cv2.imshow("frame", frame)  
  
    # setting values for base colors 
    b = frame[:, :, :1] 
    g = frame[:, :, 1:2] 
    r = frame[:, :, 2:] 
  
    # computing the mean 
    b_mean = np.mean(b) 
    g_mean = np.mean(g) 
    r_mean = np.mean(r) 
    print(r_mean, g_mean, b_mean)
