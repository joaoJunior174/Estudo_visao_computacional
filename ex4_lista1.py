# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from skimage import filters
# import scipy.misc

# img = cv2.imread('xadrez.jpeg')

#laplace
# _laplaciano = cv2.Laplacian(img,cv2.CV_64F)

#sobel
# sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# _sobel=(sx**2+sy**2)**0.5


# plt.imshow(_laplaciano),plt.title('filtro_laplaciano')
# plt.xticks([]), plt.yticks([])
# plt.savefig("_laplaciano_xadrez.png");

# plt.imshow(_sobel),plt.title('filtro_sobel')
# plt.xticks([]), plt.yticks([])
# plt.savefig("_sobel_xadrez.png");

# data=_laplaciano
# data = 255 * data # Now scale by 255
# data = data.astype(np.uint8)

# histr = cv2.calcHist([data],[0],None,[256],[0,256]) 

# plt.plot(histr) 
# plt.savefig("histograma_laplace.png")

# data=_sobel
# data = 255 * data # Now scale by 255
# data = data.astype(np.uint8)

# histr = cv2.calcHist([data],[0],None,[256],[0,256]) 

# plt.plot(histr) 
# plt.savefig("histograma_sobel.png")

# k=1
# gauss = np.random.normal(0,k/10,img.size)
# gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')

# for i in range(0,np.size(gauss, 0),1):
#   for j in range(0,np.size(gauss, 1),1):
#     if(not np.array_equal(gauss[i,j],[0,0,0])):
#       gauss[i,j]=[255,255,255]

# img = cv2.add(img,gauss)

# plt.imshow(img),plt.title('ruido_xadrez com sigma='+str(k/10))
# plt.xticks([]), plt.yticks([])
# plt.savefig("_sobel_xadrez_"+str(k/10)+".png");


#laplace
# _laplaciano = cv2.Laplacian(img,cv2.CV_64F)

#sobel
# sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# _sobel=(sx**2+sy**2)**0.5


# plt.imshow(_laplaciano),plt.title('filtro_laplaciano_xadrex_ruido_'+str(k/10))
# plt.xticks([]), plt.yticks([])
# plt.savefig("filtro_laplaciano_xadrex_ruido_"+str(k/10)+".png");

# plt.imshow(_sobel),plt.title('filtro_sobel_xadrex_ruido_'+str(k/10))
# plt.xticks([]), plt.yticks([])
# plt.savefig("filtro_sobel_xadrex_ruido_"+str(k/10)+".png");

# data=_laplaciano
# data = 255 * data # Now scale by 255
# data = data.astype(np.uint8)

# data=_sobel
# data = 255 * data # Now scale by 255
# data = data.astype(np.uint8)

# histr = cv2.calcHist([data],[0],None,[256],[0,256]) 

# plt.plot(histr) 
# plt.savefig("histograma_sobel_ruido_"+str(k/10)+".png")
