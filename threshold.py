# Threshholding

import numpy as np
import scipy.misc as misc
import matplotlib.pyplot as plt

def threshhold(image, threshold_value):
	(r, c) = image.shape
	new_image = np.zeros((r, c))
	for i in range(r):
		for j in range(c):
			if image[i,j] > threshold_value:
				new_image[i,j] = 255
			else: 
				new_image[i,j] = 0
		
	return new_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

image = misc.imread('lena.jpg')
threshold_value=input('Enter the threshhold value : ')
show_images(image, threshhold(image, threshold_value), 'Original Image', 'Threshholded Image')
