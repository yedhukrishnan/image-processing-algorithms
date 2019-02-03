# Convolution of x and h without using built-in functions

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

def convolve(x, h):
	# We are implementing graphical method.
	# We first need to find the rows and cols of both the matrices
	# as follows
	(row1, col1) = x.shape
	(row2, col2) = h.shape

	# Dimension of output matrix A is given by
	# (number of rows of x + number of rows h - 1) x (number of cols of x + number of cols of h - 1)
	# So we can define an array to store output values with that dimension
	a = np.zeros((row1 + row2 - 1, col1 + col2 - 1))

	# Now, find h(-m, -n)
	h = h[::-1,::-1]

	# Add padding zeros around the x matrix.
	# This step is a bit confusing
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

x = misc.imread('lena.jpg')
h = np.ones((4, 4)) / 16.0

output = convolve(x, h)

show_images(x, output, 'Original Image', 'Image after Convolution')
