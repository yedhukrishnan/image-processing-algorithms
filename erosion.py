# Erosion

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def erosion(image, structuring_element):
    (image_row, image_col) = image.shape
    (element_row, element_col) = structuring_element.shape

    eroded_image = np.copy(image)

    for i in range(image_row - element_row + 1):
        for j in range(image_col - element_col + 1):
            mask = image[i:i+element_row, j:j+element_col]
            overlap = structuring_element * mask
            if np.array_equal(overlap, structuring_element * 255):
                eroded_image[i, j] = 255
            else:
                eroded_image[i, j] = 0

    return eroded_image

def threshold(image):
    new_image = np.zeros(image.shape)
    (row, col) = image.shape
    for i in range(row):
        for j in range(col):
            if image[i, j] > 128:
                new_image[i, j] = 255
    return new_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

structuring_element = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ])

image = misc.imread('jjj.jpg')
image = threshold(image)

dil = erosion(image, structuring_element)
show_images(image, dil, 'Original Image', 'Image after Erosion')
