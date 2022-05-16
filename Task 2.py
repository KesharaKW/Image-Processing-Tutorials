"""
Group 5
Task 2
"""

#import the required library
import cv2

#start capturing video from webcam
cap = cv2.VideoCapture(0)

#check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

#default resolutions of the frame are obtained, and the resolutions are converted from float to integer
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#read until video is completed
while(cap.isOpened()):          #execute the code while the camera is running
  ret, frame = cap.read()  	#capture frame-by-frame
  frame = cv2.flip(frame,1) 	#flip image
  frameg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  if ret == True:
    cv2.imshow("Frame",frameg) 	#now each frame of the video becomes the image that we will be analysing
    k = cv2.waitKey(25) 	#wait for 25 ms before moving on to the next frame. This will slow down the video
    if k == 27 or k == 113:
        break			#break the loop when 'q' or 'ESC' is pressed
  else:
    break

#when everything done, release the VideoCapture and VideoWriter objects
cap.release()
cv2.destroyAllWindows()
