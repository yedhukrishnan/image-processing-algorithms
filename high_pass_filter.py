# High pass filter

import numpy as np
from scipy import misc, signal
import matplotlib.pyplot as plt

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

def convolve(x, h):
    (row1, col1) = x.shape
    (row2, col2) = h.shape

    convolved_image = np.zeros((row1 + row2 - 1, col1 + col2 - 1))

    h = h[::-1,::-1]
    b = np.lib.pad(x, [(row2 - 1, row2 - 1), (col2 - 1, col2 - 1)], mode='constant')

    for i in range(row1 + row2 - 1):
        for j in range(col1 + col2 - 1):
            k = b[i:i+row2, j:j+col2]
            temp = k * h
            convolved_image[i, j] = np.sum(temp)

    return convolved_image

image = misc.imread('gray_nature.jpg')
high_pass_filter = np.array([[1.0, 1.0, 1.0], [1.0, -8.0, 1.0], [1.0, 1.0, 1.0]])

averaged_image = convolve(image, high_pass_filter)

show_images(image, averaged_image, 'Original Image', 'Sharpened Image')
