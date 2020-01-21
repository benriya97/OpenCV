#import following packages
import numpy as np
import cv2
from matplotlib import pyplot as plt

#open image in gray-scale
img = cv2.imread('C:\\Users\\Riya Benoy\\Desktop\\OpenCV\\Project-2\\Singapore.jpg',0)

#when displaying, show a blurred (bicubic) image
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])  

#display image
plt.show()