"""
Group 5
Task 1.1
"""
#import the required library
import cv2

#read the image 
my_image = cv2.imread("lena.jpg",1)

#enter the code block to display the image
#cv2.imshow("lena",my_image)
#cv2.waitKey(0)

k = 0
#Use the ASCII code for relevant character
#Example 113 for character q
while k != (113):
    cv2.imshow("lena",my_image)
    k = cv2.waitKey(0) & 0xFF
