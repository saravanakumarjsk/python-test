
#for this program to work you must save it in the file/folder where your pic is
#saved


import numpy as np
import cv2

img = cv2.imread('watch.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyALLWindows()
