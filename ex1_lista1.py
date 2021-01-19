import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('LENNA.jpeg')
medianFilter = cv2.blur(img,(5,5))
medianFilter3 = medianFilter
medianFilter4 = medianFilter
medianFilter3 = cv2.blur(medianFilter3,(5,5))
medianFilter4 = cv2.blur(medianFilter4,(5,5))

for i in range(0,5,1):
  medianFilter3 = cv2.blur(medianFilter3,(5,5))

for i in range(0,10,1):
  medianFilter4 = cv2.blur(medianFilter4,(5,5))

plt.subplot(2,2,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(medianFilter),plt.title('filtro aplicado uma vez')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(medianFilter3),plt.title('filtro aplicado cinco vezes')
plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(medianFilter4),plt.title('filtro aplicado dez vezes')
plt.xticks([]), plt.yticks([])
plt.savefig("Exercicio1.png");
