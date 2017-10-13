import numpy as np
import cv2
import matplotlib.pylab as plt

import sys

vidcap = cv2.VideoCapture(sys.argv[1])

success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  cv2.imwrite("images/frame%04d.jpg" % count, image)     # save frame as JPEG file
  count += 1



