
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
from dit.other import tsallis_entropy
from dit import Distribution


image = cv2.imread('cancer_image_1.png',0)

maior=-1
indexg = -1
indexk = -1
for g in range(1,256,16):
  for k in range(g+16,256,16):
    img=np.copy(image)
    for i in range(0,np.size(img, 0),1):
      for j in range(0,np.size(img, 1),1):
        if(img[i,j] <= g):
          img[i,j]=0;
        elif(img[i,j]>g and img[i,j]<=k):
          img[i,j] = 50;
        else:
          img[i,j] = 255;

    histg = cv2.calcHist([img],[0],None,[256],[0,256]) 

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
    vlr = tsallis_entropy(dist, 2)

    if(vlr > maior):
      maior=vlr;
      indexg=g
      indexk=k;

  

print(indexg)
print(indexk)

for i in range(0,np.size(image, 0),1):
  for j in range(0,np.size(image, 1),1):
    if(image[i,j] <= indexg):
      image[i,j]=0;
    elif(image[i,j]>indexg and image[i,j]<=indexk):
      image[i,j] = 100;
    else:
      image[i,j] = 255;



kernel = np.ones((5,5), np.uint8) 
  
 
img_dilation = cv2.dilate(image, kernel, 
iterations=2) 
img_erosion = cv2.erode(img_dilation,
kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion,
kernel, iterations=2) 
img_erosion = cv2.erode(img_dilation,
kernel, iterations=3)
img_dilation = cv2.dilate(img_erosion,
kernel, iterations=2)
img_erosion = cv2.erode(img_dilation, 
kernel, iterations=3)
img_dilation = cv2.dilate(img_erosion, 
kernel, iterations=6)
img_erosion = cv2.erode(img_dilation,
kernel, iterations=3)
img_dilation = cv2.dilate(img_erosion,
kernel, iterations=6)
img_erosion = cv2.erode(img_dilation,
kernel, iterations=6)

image = img_erosion

for i in range(0,np.size(image, 0),1):
  for j in range(0,np.size(image, 1),1):
 if (image[i,j] == 0):
   image[i,j] = 255
 else:
   image[i,j] = 0

plt.imshow(image, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig("cancer_image_1_final.png")
