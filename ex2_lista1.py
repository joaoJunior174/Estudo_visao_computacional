import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('natureza.jpeg')
output1 = cv2.GaussianBlur(img,(3,3),0.1)
output2 = cv2.GaussianBlur(img,(3,3),0.2)
output3 = cv2.GaussianBlur(img,(3,3),0.3)
output4 = cv2.GaussianBlur(img,(3,3),0.4)
output5 = cv2.GaussianBlur(img,(3,3),0.5)
output6 = cv2.GaussianBlur(img,(3,3),0.6)
output7 = cv2.GaussianBlur(img,(3,3),0.7)
output8 = cv2.GaussianBlur(img,(3,3),0.8)
output9 = cv2.GaussianBlur(img,(3,3),0.9)
output10 = cv2.GaussianBlur(img,(3,3),1)
plt.imshow(output10),plt.title('sigma=1')
plt.xticks([]), plt.yticks([])
plt.savefig("img10.png");
