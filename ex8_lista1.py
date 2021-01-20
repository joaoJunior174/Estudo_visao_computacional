import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import scipy.misc
import io, os

img = cv2.imread('forest.jpeg')

for i in range(1,21,1):
  print("iteração:"+str(i))
  img = cv2.blur(img,(5,5))
  plt.imshow(img),
  plt.xticks([]), plt.yticks([])
  plt.savefig("compactJPG_"+str(i)+".jpeg");
