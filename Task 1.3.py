"""
Group 5
Task 1.3
"""
#import the required library
import cv2

#read the image 
capsicum = cv2.imread("capsicum.jpg",1)

#convert the image to HSV
imageHSV = cv2.cvtColor(capsicum,cv2.COLOR_BGR2HSV)

#create the red color mask

mask1 = cv2.inRange(imageHSV,(0,100,0),(5,255,255))
mask2 = cv2.inRange(imageHSV,(175,100,0),(180,255,255))

mask = mask1+mask2

#display the mask
cv2.imshow("RedMask",mask)
#cv2.imshow()
