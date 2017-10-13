import numpy as np
import cv2

img0 = cv2.imread('img0.jpg')
img1 = cv2.imread('img1.png')

cv2.imshow('image',img0)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



