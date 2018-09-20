# Motion blur

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def convolve(x, h):
	(row1, col1) = x.shape
	(row2, col2) = h.shape

	a = np.zeros((row1 + row2 - 1, col1 + col2 - 1))
	h = h[::-1,::-1]
	b = np.lib.pad(x, [(row2 - 1, row2 - 1), (col2 - 1, col2 - 1)], mode='constant')

	for i in range(row1 + row2 - 1):
	    for j in range(col1 + col2 - 1):
	        k = b[i:i+row2, j:j+col2]
	        temp = k * h
	        a[i, j] = np.sum(temp)

	return a

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()


# generating the kernel
size = 15
kernel = np.zeros((size, size))
kernel[int((size-1)/2), :] = np.ones(size)
kernel = kernel / size

image = misc.imread('gray_sign.jpg')
motion_blurred_image = convolve(image, kernel)
show_images(image, motion_blurred_image, 'Original Image', 'Motion Blurred Image')
