import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('rocks.jpeg',0)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
titles = ['Imagem original',
            'Limiar adaptativo (media)', 'Limiar adaptativo (Gaussiano)']
images = [img, th2, th3]
for i in range(0,3,1):
  plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
plt.savefig('aas.jpeg')
