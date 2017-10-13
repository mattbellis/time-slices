import numpy as np
import cv2
import matplotlib.pylab as plt

def dist(a,b):

    #d0 = (a[0]-b[0])
    #d1 = (a[1]-b[1])
    #d2 = (a[2]-b[2])

    diff = a-b

    return np.sqrt((diff*diff).sum())


img0 = cv2.imread('img0.jpg')
img1 = cv2.imread('img1.png')

lx = len(img0)
ly = len(img0[0])

imgnew = img0.copy()

dists = []
for i in range(0,lx):
    for j in range(0,ly):
        val0 = img0[i][j]
        val1 = img1[i][j]

        r = dist(val0,val1)
        dists.append(r)

        if r>28:
            imgnew[i][j] = val1

#plt.hist(dists)
#plt.show()

#imgnew = img0 + img1

cv2.imshow('image',imgnew)
cv2.imshow('image0',img0)
cv2.imshow('image1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.imshow('image',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



