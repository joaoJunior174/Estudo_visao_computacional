
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
from dit.other import tsallis_entropy
from dit import Distribution


image = cv2.imread('cancer_image_2.png',0)

indexg = 49
indexk = 81


for i in range(0,np.size(image, 0),1):
  for j in range(0,np.size(image, 1),1):
    if(image[i,j] <= indexg):
      image[i,j]=0;
    elif(image[i,j]>indexg and image[i,j]<=indexk):
      image[i,j] = 100;
    else:
      image[i,j] = 255;



kernel = np.ones((5,5), np.uint8) 
  
 
img_dilation = cv2.dilate(image, kernel, iterations=1) 
img_erosion = cv2.erode(img_dilation, kernel, iterations=7)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=13) 
img_erosion = cv2.erode(img_dilation, kernel, iterations=5)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=6)

image = img_dilation

for i in range(0,np.size(image, 0),1):
  for j in range(0,np.size(image, 1),1):
    if (image[i,j] == 0):
      image[i,j] = 255
    else:
      image[i,j] = 0

plt.imshow(image, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig("cancer_image_2_erosion_transform_final.png")
