
import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import scipy.misc


img = cv2.imread('circulos.png')

circuloMaior = np.copy(img)
circuloMenor = np.copy(img)


for i in range(0,np.size(circuloMaior, 1),1):
  for j in range(0,np.size(circuloMaior, 0),1):
    if(not (np.array_equal(circuloMaior[j][i],[100,100,100]) or np.array_equal(circuloMaior[j][i],[50,50,50]))):
      circuloMaior[j,i] = [0,0,0]
    else:
      circuloMaior[j,i] = [255,255,255]  

cor=[0,0,0]

img2=np.copy(circuloMaior)
img3=np.copy(circuloMaior)

for i in range(0,np.size(img2, 1),1):
  for j in range(0,np.size(img2, 0),1):
    if(not np.array_equal(img2[j][i],cor)):
      img2[j,i] = [255,255,255]
      if(np.array_equal(cor,[0,0,0])):
        cor=[255,255,255] 
      else:
        cor=[0,0,0]
    else:
      img2[j,i]=[0,0,0]

cor=[0,0,0]

for i in range(0,np.size(img3, 0),1):
  for j in range(0,np.size(img3, 1),1):
    if(not np.array_equal(img3[i,j],cor)):
      img3[i,j] = [255,255,255]
      if(np.array_equal(cor,[0,0,0])):
        cor=[255,255,255] 
      else:
        cor=[0,0,0]
    else:
      img3[i,j]=[0,0,0]

img4 = (img3**2+img2**2)**0.5 



for i in range(0,np.size(circuloMenor, 1),1):
  for j in range(0,np.size(circuloMenor, 0),1):
    if(not (np.array_equal(circuloMenor[j][i],[50,50,50]))):
      circuloMenor[j,i] = [0,0,0]
    else:
      circuloMenor[j,i] = [255,255,255]  

cor=[0,0,0]

img2=np.copy(circuloMenor)
img3=np.copy(circuloMenor)

for i in range(0,np.size(img2, 1),1):
  for j in range(0,np.size(img2, 0),1):
    if(not np.array_equal(img2[j][i],cor)):
      img2[j,i] = [255,255,255]
      if(np.array_equal(cor,[0,0,0])):
        cor=[255,255,255] 
      else:
        cor=[0,0,0]
    else:
      img2[j,i]=[0,0,0]

cor=[0,0,0]

for i in range(0,np.size(img3, 0),1):
  for j in range(0,np.size(img3, 1),1):
    if(not np.array_equal(img3[i,j],cor)):
      img3[i,j] = [255,255,255]
      if(np.array_equal(cor,[0,0,0])):
        cor=[255,255,255] 
      else:
        cor=[0,0,0]
    else:
      img3[i,j]=[0,0,0]

img5 = (img3**2+img2**2)**0.5 

plt.imshow(img4),plt.title('circulo maior')
plt.xticks([]), plt.yticks([])
plt.savefig("maior.png");

plt.imshow(img5),plt.title('circulo menor')
plt.xticks([]), plt.yticks([])
plt.savefig("menor.png");


padrao_ouro = (img5**2 + img4**2)**0.5

#parte com ruido
for k in range(1,6,1):

  img = cv2.imread('circulos.png')

  gauss = np.random.normal(0,k/10,img.size)
  gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

  for i in range(0,np.size(gauss, 0),1):
    for j in range(0,np.size(gauss, 1),1):
      if(not np.array_equal(gauss[i,j],[0,0,0])):
        gauss[i,j]=[255,255,255]

  img = cv2.add(img,gauss)


  _laplaciano = cv2.Laplacian(img,cv2.CV_64F)

  sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
  sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
  _sobel=(sx**2+sy**2)**0.5

  edges = filters.prewitt(img)


  for i in range(0,np.size(_laplaciano, 0),1):
    for j in range(0,np.size(_laplaciano, 1),1):
      if(not np.array_equal(_laplaciano[i,j],[0,0,0])):
        _laplaciano[i,j] = 255;

  for i in range(0,np.size(_sobel, 0),1):
    for j in range(0,np.size(_sobel, 1),1):
      if(not np.array_equal(_sobel[i,j],[0,0,0])):
        _sobel[i,j] = 255;

  
  inter_laplaciano = 0;
  union_laplaciano = 0;

  inter_sobel = 0;
  union_sobel = 0;

  inter_prewitt = 0;
  union_prewitt = 0;

  for i in range(0,np.size(_laplaciano, 0),1):
    for j in range(0,np.size(_laplaciano, 1),1):
      if(not np.array_equal(_laplaciano[i,j],[0,0,0])):
        union_laplaciano+=1
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          inter_laplaciano+=1
      else:
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          union_laplaciano+=1

  for i in range(0,np.size(_sobel, 0),1):
    for j in range(0,np.size(_sobel, 1),1):
      if(not np.array_equal(_sobel[i,j],[0,0,0])):
        union_sobel+=1
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          inter_sobel+=1
      else:
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          union_sobel+=1    

  for i in range(0,np.size(edges, 0),1):
    for j in range(0,np.size(edges, 1),1):
      if(not np.array_equal(edges[i,j],[0,0,0])):
        union_prewitt+=1
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          inter_prewitt+=1
      else:
        if(not np.array_equal(padrao_ouro[i,j],[0,0,0])):
          union_prewitt+=1
  print("-------------------------------------")
  print(k/10)
  print(inter_laplaciano/union_laplaciano)
  print(inter_sobel/union_sobel)
  print(inter_prewitt/union_prewitt)

  plt.imshow(_sobel),plt.title('sobel'+str(k))
  plt.xticks([]), plt.yticks([])
  plt.savefig("sobel"+str(k)+".png");

  plt.imshow(_laplaciano),plt.title('laplaciano'+str(k))
  plt.xticks([]), plt.yticks([])
  plt.savefig("laplaciano"+str(k)+".png");

  plt.imshow(edges),plt.title('prewitt'+str(k))
  plt.xticks([]), plt.yticks([])
  plt.savefig("prewitt"+str(k)+".png");
