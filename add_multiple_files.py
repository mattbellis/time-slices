import numpy as np
import cv2
import matplotlib.pylab as plt
import sys

def dist(a,b):

    mat = np.zeros((len(a),len(a[0])))

    diff = b.astype(int) - a.astype(int)
    #print(diff)

    diff *= diff
    #print(diff)

    for i in range(0,len(a)):
        for j in range(0,len(a[i])):
            mat[i][j] = diff[i][j].sum()

    return mat


images = sys.argv[1:]
nimages = len(images)


starter_image = cv2.imread(images[0])

lx = len(starter_image)
ly = len(starter_image[0])

newimg = starter_image.copy()

for i in range(1,nimages):

    print(images[i])

    img = cv2.imread(images[i])

    print("---------")

    #diff = img.astype(int) - starter_image.astype(int)

    diff = dist(img,starter_image)
    print(diff)
    print(len(diff.flatten()))
    print(len(img),len(img[0]))


    #diff = img - starter_image
    #dist = diff*diff

    #print(diff)
    #print("========")
    #print(dist)

    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    change_pixels = diff>2000

    #plt.hist(diff.flatten(),bins=1000)
    #plt.show()

    newimg[change_pixels] = img[change_pixels]



cv2.imshow('image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('newimage.png',newimg)


#cv2.waitKey(0)
#cv2.destroyAllWindows()

#cv2.imshow('image',img1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()



