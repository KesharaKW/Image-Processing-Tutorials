"""
Group 5
Task 3
"""

#import required libraries
import cv2

#read the images
opening = cv2.imread("opening.png",1)
closing = cv2.imread("closing.png",1)

#specify kernal size
kernal = 8


#create the structuring element
element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3*kernal+1,3*kernal+1))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3*kernal+1,3*kernal+1))

#create the Opening morphological mask
mask1 = cv2.morphologyEx(opening,cv2.MORPH_OPEN, element1)

#create the Closing morphological mask 
mask2 = cv2.morphologyEx(closing,cv2.MORPH_CLOSE, element2)

#display the results
cv2.imshow("Opening",mask1)
cv2.imshow("Closing",mask2)
