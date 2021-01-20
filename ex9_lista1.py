import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import filters
import scipy.misc
import io, os

img = cv2.imread('caveira.png')


#(a)

l_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
_laplaciano = cv2.filter2D(img, -1, l_kernel)

plt.imshow(_laplaciano),plt.xticks([]), plt.yticks([])
plt.savefig("(a).png");

#(b)
_realce = cv2.add(_laplaciano,img)

plt.imshow(_realce),plt.xticks([]), plt.yticks([])
plt.savefig("(b).png");

#(c)
sx = cv2.Sobel(_laplaciano,cv2.CV_64F,1,0,ksize=3)
sy = cv2.Sobel(_laplaciano,cv2.CV_64F,0,1,ksize=3)
_sobel=(sx**2+sy**2)**0.5

plt.imshow(_sobel),plt.xticks([]), plt.yticks([])
plt.savefig("(c).png");

#(d)
_medianFilter = cv2.blur(_sobel,(5,5))
data=_medianFilter
data = 255 * data
_medianFilter = data.astype(np.uint8)

plt.imshow(_medianFilter),plt.xticks([]), plt.yticks([])
plt.savefig("(d).png");

#(e)
_mask = cv2.add(_realce,_medianFilter)
plt.imshow(_mask),plt.xticks([]), plt.yticks([])
plt.savefig("(e).png");

#(f)
_finalSum = cv2.add(img,_mask)

plt.imshow(_finalSum),plt.xticks([]), plt.yticks([])
plt.savefig("(f).png");

#(g) 
gamma=1.2
_finalResult = np.array(255*(_finalSum / 255) ** gamma, dtype = 'uint8') 

plt.imshow(_finalResult),plt.xticks([]), plt.yticks([])
plt.savefig("(g).png");
