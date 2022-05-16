"""
 2022 ME515 MECHATRONICS LAB : Color Detector Project
 prepared by M.Wickramasuriya  maneeshaw@eng.pdn.ac.lk
             S.Rajinth         rajinthss@eng.pdn.ac.lk
"""

#import module
import cv2
import numpy as np

#capture video from webcam
cap = cv2.VideoCapture(0)

#check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

#read until video is completed
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    #convert to HSV
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #detect Blue color mask
    FrameBlue = cv2.inRange(frameHSV, (0, 0, 0), (5, 255, 255))

    #do necessory morpological transformations
    k = 6
    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3*k+1,3*k+1))
    mask1 = cv2.morphologyEx(FrameBlue,cv2.MORPH_OPEN, element)
    blue = cv2.bitwise_and(frame, frame, mask = mask1)
    maskGray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)

    #track the blue bottle cap using contour method
    contours,hierarchy = cv2.findContours(maskGray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    cv2.drawContours(mask1, contours, -1, (0,255,0), 3);
    
    for cnt in contours:
        M = cv2.moments(cnt)
        x = int(round(M["m10"]/M["m00"]))
        y = int(round(M["m01"]/M["m00"]))
        cv2.circle(frame, (x,y), 10, (255,0,0), -1);
 
        
    if ret == True:
        cv2.imshow("Image", frame)
        cv2.imshow("Isolated color", blue)
        k = cv2.waitKey(25)
        if k==27 or k==113:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



