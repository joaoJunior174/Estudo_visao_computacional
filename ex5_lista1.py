# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from skimage import filters
# import scipy.misc
# from scipy.fft import fft, ifft

# img = cv2.imread('caozinho.jpeg',0)

# sx_1 = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
# sy_1 = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)


# f = np.fft.fft2(sy_1)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))



# plt.subplot(121),plt.imshow(sy_1, cmap='gray')
# plt.title('Sobel na vertical'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap='gray')
# plt.title('Fourier em sobel na vertical'), plt.xticks([]), plt.yticks([])

#provando a distributividade

# F(f(x,y) + f(a,b)) = F(f(x,y)) + F(f(a,b))

#F(f(x,y) + f(a,b))
# soma=(sx_1**2+sy_1**2)**0.5
# f = np.fft.fft2(soma)
# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))


#F(f(x,y)) + F(f(a,b))
# f = np.fft.fft2(sx_1)
# fshift = np.fft.fftshift(f)
# sx_1 = 20*np.log(np.abs(fshift))
# f = np.fft.fft2(sy_1)
# fshift = np.fft.fftshift(f)
# sy_1 = 20*np.log(np.abs(fshift))

# soma=(sx_1**2+sy_1**2)**0.5

#provando a propriedade de multiplicação

# soma=(sx_1**2+sy_1**2)**0.5

# soma=0.5*soma;
# f = np.fft.fft2(soma)
# fshift = np.fft.fftshift(f)
# output_1 = 20*np.log(np.abs(fshift))

# soma=(sx_1**2+sy_1**2)**0.5
# f = np.fft.fft2(soma)
# fshift = np.fft.fftshift(f)
# output_2 = 20*np.log(np.abs(fshift))
# output_2=0.5*output_2

# plt.subplot(121),plt.imshow(output_1, cmap='gray')
# plt.title('af(x,y)'), plt.xticks([]), plt.yticks([])

# plt.subplot(122),plt.imshow(output_2, cmap='gray')
# plt.title('aF(u,v)'), plt.xticks([]), plt.yticks([])


# plt.savefig("fourier_multiplicacao.jpeg")
