# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from skimage import filters
# import scipy.misc
# from scipy.fft import fft, ifft

# img = cv2.imread('caozinho.jpeg',0)

# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))



#questão 1
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Imagem original'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('FFT'), plt.xticks([]), plt.yticks([])
# plt.savefig('dog_fft_normal.png')

#questãão 2

# img = cv2.imread('caozinho.jpeg',0)

# dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)

# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))


# rows, cols = img.shape
# crow,ccol = int(rows/2) , int(cols/2)

# create a mask first, center square is 1, remaining all zeros
# mask = np.zeros((rows,cols,2),np.uint8)
# mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# apply mask and inverse DFT
# fshift = dft_shift*mask
# f_ishift = np.fft.ifftshift(fshift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Imgem original'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Imagem com polda em baixa frequêência'), plt.xticks([]), plt.yticks([])
# plt.savefig('low_frequence_filtering.png')


# rows, cols = img.shape
# crow,ccol = int(rows/2) , int(cols/2)
# fshift[crow-30:crow+31, ccol-30:ccol+31] = 0
# f_ishift = np.fft.ifftshift(fshift)
# img_back = np.fft.ifft2(f_ishift)
# img_back = np.real(img_back)
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
# plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])


# plt.savefig("high_frequence_filtering.png")

#filtro da media
# img = cv2.medianBlur(img,5)

#filtro da mediana
# img = cv2.blur(img,(5,5))

#filtro de sobel
# sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# img=(sx**2+sy**2)**0.5

#filtro de suavizaçãão Gaussiano
# img = cv2.GaussianBlur(img,(5,5),0)

# f = np.fft.fft2(img)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))

# plt.imshow(img),plt.title('filtro da media')
# plt.xticks([]), plt.yticks([])
# plt.savefig("fourier_filtro_media.png");

# plt.subplot(121),plt.imshow(img)
# plt.title('Imagem com o filtro'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('FTT'), plt.xticks([]), plt.yticks([])
# plt.savefig('fourier_filtro_gaussiano_espectro.png')

#calculo gradiente

# sx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

#gradiente total

# total = (sx**2 + sy**2)**0.5

# plt.subplot(121),plt.imshow(sx)
# plt.title('Gradiente na horizontal'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(sy, cmap = 'gray')
# plt.title('Gradiente na vertical'), plt.xticks([]), plt.yticks([])
# plt.savefig('calculo_gradiente.png')
