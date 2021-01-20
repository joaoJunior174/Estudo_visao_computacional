import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import skimage.measure    

img = cv.imread('rocks.jpeg',0)

maxEntropy = -1;
limiar = 1;

for p in range(1,255,1):
  aux=np.copy(img);
  for i in range(0,np.size(aux, 0),1):
    for j in range(0,np.size(aux, 1),1):
      if (aux[i,j] >= p):  
          aux[i,j] = 255;
      else:
        aux[i,j] = 0;
  entropy = skimage.measure.shannon_entropy(aux)
  
  if(entropy > maxEntropy):
    maxEntropy = entropy
    limiar = p;

aux=np.copy(img);
for i in range(0,np.size(aux, 0),1):
  for j in range(0,np.size(aux, 1),1):
    if (aux[i,j] >= limiar):  
      aux[i,j] = 255;
    else:
      aux[i,j] = 0;



plt.imshow(aux,cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig("threshold.png");
