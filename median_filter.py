# Median filter

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def median_filter(image):
    (row, col) = image.shape

    # Define a matrix to store the new image
    filtered_image = np.zeros(image.shape)

    # Pad the original image with zeros to apply median filter
    image = np.lib.pad(image, [(1, 1), (1, 1)], mode='constant')

    for i in range(row):
        for j in range(col):
            # Find the elements in the mask
            mask = image[i:i+3, j:j+3]
            # Sort the elements
            mask = np.sort(mask.flatten())
            # Find the middle element, which is the median
            # In a 3x3 matrix, middle element will be at position 4
            filtered_image[i, j] = mask[4]

    return filtered_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()


image = misc.imread('gray_sign.jpg')
show_images(image, median_filter(image), 'Original Image', 'Median Filtered Image')
