#import numpy and cv2 packages
import numpy as np  
import cv2

#open image Singapore.jpg in gray (1 for color, 0 for grayscale, and -1 for unchanged)
img = cv2.imread("C:\\Users\\Riya Benoy\\Desktop\\OpenCV\\Project-1\\Singapore.jpg",0)

#cv2.WINDOW_NORMAL helps to resize image on screen, else use cv2.WINDOW_AUTOSIZE
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#display image on screen
cv2.imshow('image',img)

#arguement 0 is used to take an action when a key is pressed, and that state is saved in k 
k=cv2.waitKey(0)

#if keyboard key 'e' is pressed, escape action is done, where the displayed image is closed
if k == ord('e'):
    cv2.destroyAllWindows()

#if keyboard key 's' is pressed, save action is done, where the grayscaled image is saved and closed
elif k == ord('s'): 
    cv2.imwrite("C:\\Users\\Riya Benoy\\Desktop\\OpenCV\\Project-1\\SingaporeGray.jpg",img)
    cv2.destroyAllWindows()
