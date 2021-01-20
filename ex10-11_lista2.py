import numpy as np
import math 
import matplotlib.pyplot as plt 
import cv2 
from dit.other import tsallis_entropy
from dit import Distribution


def getKulbackDistance(A,B):
  
  data=A
  data = 255 * data
  A = data.astype(np.uint8)

  data=B
  data = 255 * data
  B = data.astype(np.uint8)

  histA = cv2.calcHist([A],[0],None,[256],[0,256]) 
  histB = cv2.calcHist([B],[0],None,[256],[0,256])

  soma=0;
  for i in histA:
    soma=soma+i[0]

  for i in range(0,256,1):
    histA[i][0]=histA[i][0]/soma

  soma=0;
  for i in histB:
    soma=soma+i[0]

  for i in range(0,256,1):
    histB[i][0]=histB[i][0]/soma

  soma_1 = 0
  soma_2 = 0
  A = histA
  B = histB

  for i in range(0,len(A),1):
   soma_1 = A[i,0]*math.log(A[i,0]/B[i,0])+soma_1

  for i in range(0,len(B),1):
    soma_2 = B[i,0]*math.log(B[i,0]/A[i,0])+soma_2

  return soma_1+soma_2

def getVectorialDistance(A,B):
  data=A
  data = 255 * data
  A = data.astype(np.uint8)

  data=B
  data = 255 * data
  B = data.astype(np.uint8)

  histA = cv2.calcHist([A],[0],
                      None,
                      [256],
                      [0,256]) 
  histB = cv2.calcHist([B],
                      [0],
                      None,
                      [256],
                      [0,256])

  soma=0;
  for i in histA:
    soma=soma+i[0]

  for i in range(0,256,1):
    histA[i][0]=histA[i][0]/soma

  soma=0;
  for i in histB:
    soma=soma+i[0]

  for i in range(0,256,1):
    histB[i][0]=histB[i][0]/soma

  A = histA
  B = histB
  up=0
  down_1=0
  down_2=0

  for i in range(0,len(A),1):
    up = A[i,0]*B[i,0] + up
    down_1 = A[i,0]*A[i,0]+down_1
    down_2 = B[i,0]*B[i,0]+down_2
  
  return up/(down_1**0.5 + down_2**0.5)



def getEuclideanDistance(A,B):
  soma = 0
  for i in A:
    aux = getMinimumDistance(i,B)
    soma = soma + aux
  return soma**0.5


def getPolylineDistanceMeasure(A,B):
  soma_1 = 0
  soma_2 = 0
  for i in A:
    aux = getMinimumDistance(i,B)
    soma_1 = soma_1 + aux

  for i in B:
    aux = getMinimumDistance(i,A)
    soma_2 = soma_2 + aux

  return (soma_1+soma_2)/(len(A)+len(B))

def getHausdorffDistance(A,B):
  maxDistance_1 = -1
  maxDistance_2 = -1
  for i in A:
    aux = getMinimumDistance(i,B)
    if(aux >maxDistance_1):
      maxDistance_1 = aux;

  for i in B:
    aux = getMinimumDistance(i,A)
    if(aux > maxDistance_2):
      maxDistance_2 = aux;

  if(maxDistance_1 > maxDistance_2):
    return maxDistance_1

  return maxDistance_2

def getMinimumDistance(A,B):
  minimum=100000
  for i in B:
    distance = ((A[0]-i[0])**2 + 
               (A[1]-i[1])**2)**0.5
    if(distance < minimum):
      minimum=distance
  return distance

def getClosestPoint(A,B):
  minimum=100000
  point=[]
  for i in B:
    distance = ((A[0]-i[0])**2 + 
               (A[1]-i[1])**2)**0.5
    if(distance < minimum):
      minimum=distance
      point=i
  return point

# img1_original = cv2.imread('img_1_original.png',0)
# img1_output = cv2.imread('img_1_output.png',0)

img1_original = cv2.imread('img_2_original.png',0)
img1_output = cv2.imread('img_2_output.png',0)

sx = cv2.Sobel(img1_original,
               cv2.CV_64F,
               1,
               0,
               ksize=5)
sy = cv2.Sobel(img1_original,
              cv2.CV_64F,
              0,
              1,
              ksize=5)
img1_original=(sx**2+sy**2)**0.5


sx = cv2.Sobel(img1_output,cv2.CV_64F,
               1,
               0,
               ksize=5)
sy = cv2.Sobel(img1_output,
               cv2.CV_64F,
               0,
               1,
               ksize=5)
img1_output=(sx**2+sy**2)**0.5

original = []
output = []

for i in range(0,np.size(img1_original, 0),1):
  for j in range(0,np.size(img1_original, 1),1):
    if(img1_original[i,j]!=0):
      original.append([i,j])

for i in range(0,np.size(img1_output, 0),1):
  for j in range(0,np.size(img1_output, 1),1):
    if(img1_output[i,j]!=0):
      output.append([i,j])



print(getHausdorffDistance(original,output))
print(getPolylineDistanceMeasure(original,output))
print(getEuclideanDistance(original,output))
print(getVectorialDistance(img1_original,img1_output))
print(getKulbackDistance(img1_original,img1_output))

plt.imshow(img1_output, cmap = 'gray')
plt.xticks([]), plt.yticks([])
plt.savefig("borda_img2_output.png")
