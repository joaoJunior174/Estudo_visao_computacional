import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
from dit.other import tsallis_entropy
from dit import Distribution


image = cv2.imread('caozinho.jpeg',0)
maior=-1
index=-1
for k in range(1,256,1):

  img=np.copy(image)
  for i in range(0,np.size(img, 0),1):
    for j in range(0,np.size(img, 1),1):
      if(img[i,j] > k):
        img[i,j]=255;
      else:
        img[i,j] = 0;  

  histg = cv2.calcHist([img],[0],None,
  [256],[0,256]) 

  soma=0;
  for i in histg:
    soma=soma+i[0]

  for i in range(0,256,1):
    histg[i][0]=histg[i][0]/soma

  pair=[]
  histograma=[]

  for i in range(0,256,1):
    if(i<10):
      pair.append('00'+str(i))
    elif(i>=10 and i<100):
      pair.append('0'+str(i))
    else:
      pair.append(str(i))

  for i in histg:
    histograma.append(i[0])


  dist = Distribution(pair,histograma)
  vlr = tsallis_entropy(dist, 0.5)

  if(vlr > maior):
    maior=vlr;
    index=k

  

for i in range(0,np.size(image, 0),1):
  for j in range(0,np.size(image, 1),1):
    if(image[i,j] > index):
      image[i,j]=255;
    else:
      image[i,j] = 0; 


print(index)

# plt.imshow(image, cmap = 'gray')
# plt.xticks([]), plt.yticks([])
# plt.savefig("aaamaca.jpeg")
