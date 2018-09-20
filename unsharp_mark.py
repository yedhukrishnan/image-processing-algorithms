# Unsharp masking

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.ndimage import filters

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


image = misc.imread('gray_sign.jpg')
# Find the blurred image
blurred_image = filters.gaussian_filter(image, sigma=2, truncate=0.75)
# Subtract the blurred image from the original image
subtracted_image = image - blurred_image
# Add the subtracted image to the original image with a weighting fraction
new_image = image + 0.1 * subtracted_image

show_images(image, new_image, 'Original Image', 'Unsharp Masked Image')
