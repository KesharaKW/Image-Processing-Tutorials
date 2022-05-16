"""
Group 5
Task 1.2
"""
#import the required library
import cv2

#read the image 
tiger = cv2.imread("panther.png",1)

#Extract the R channel (3rd channel)
#cv2.imshow()
imageR = tiger[:,:,2]

#Display the original image and R channel 
cv2.imshow("panther",tiger)
cv2.imshow("ChannelR",imageR)
cv2.waitKey(0)
