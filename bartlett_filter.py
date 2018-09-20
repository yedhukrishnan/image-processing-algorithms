# Bartlett filter

import numpy as np
from scipy import misc, signal
import matplotlib.pyplot as plt

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

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

# Load the image
image = misc.imread('gray_sign.jpg')

# Generate the Bartlett filter by convolving two 3x3 averaging filters
average_filter = np.ones((3, 3)) / 9.0
bartlett_filter = convolve(average_filter, average_filter)

filtered_image = convolve(image, bartlett_filter)
show_images(image, filtered_image, 'Original Image', 'Bartlett Filtered Image')
