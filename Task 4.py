"""
Group 5
Task 4
"""

#import the required libraries
import cv2
import numpy as np

#read the image
image = cv2.imread('CoinsA.png')
imageCopy = image.copy()

# Convert to grayscale
imageHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
imageGray = cv2.inRange(imageHSV,(100,180,0),(250,255,255))

#Specify Kernal Size
kernal = 8

#Create the structuring element
element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3*kernal+1,3*kernal+1))

#Create the opening morphological mask
imageGray2 = cv2.morphologyEx(imageGray,cv2.MORPH_CLOSE, element1)

# Display images 
cv2.imshow("original",image)
cv2.imshow("grayscale",imageGray)
cv2.imshow("grayscale2",imageGray2)

# Find all contours in the image
contours, hierarchy = cv2.findContours(imageGray2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours found = {}".format(len(contours)))
print("\nHierarchy : \n{}".format(hierarchy))

# Draw all the contours
cv2.drawContours(image, contours, -1, (0,255,0), 3);
cv2.imshow("image",image)
cv2.waitKey(0)

# Find external contours in the image
#contours, hierarchy = cv2.findContours(imageGray2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#print("Number of contours found = {}".format(len(contours)))
#image = imageCopy.copy()

# Draw all the contours
#cv2.drawContours(image, contours, -1, (0,255,0), 3);
#cv2.imshow("image",image)
#cv2.waitKey(0)


for cnt in contours:
    # We will use the contour moments
    # to find the centroid
    M = cv2.moments(cnt)
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))

    # Mark the center
    cv2.circle(image, (x,y), 10, (255,0,0), -1);

cv2.imshow("image",image)
cv2.waitKey(0)

for index,cnt in enumerate(contours):
    # We will use the contour moments
    # to find the centroid
    M = cv2.moments(cnt)
    x = int(round(M["m10"]/M["m00"]))
    y = int(round(M["m01"]/M["m00"]))
    
    # Mark the center
    cv2.circle(image, (x,y), 10, (255,0,0), -1);
    
    # Mark the contour number
    cv2.putText(image, "{}".format(index + 1), (x+40, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2);

imageCopy = image.copy()

cv2.imshow("image",image)
cv2.waitKey(0)

for index,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    print("Contour #{} has area = {} and perimeter = {}".format(index+1,area,perimeter))



