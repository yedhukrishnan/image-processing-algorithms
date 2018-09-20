# Hit or Miss Transform

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

def intersection(image1, image2):
    (row, col) = image1.shape

    intersection_image = np.zeros(image1.shape)
    for i in range(row):
        for j in range(col):
            if image1[i, j] == image2[i, j] == 255:
                intersection_image[i, j] = 255

    return intersection_image

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
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])

structuring_element_compliment = 1 - structuring_element

image = misc.imread('jjj.jpg')

eroded_image = erosion(image, structuring_element)
eroded_image_complement = erosion(255 - image, structuring_element_compliment)
hit_or_missed_image = intersection(eroded_image, eroded_image_complement)

dil = erosion(image, structuring_element)
# show_images(image, eroded_image, 'Original Image', 'Hit or Miss')
# show_images(image, eroded_image_complement, 'Original Image', 'Hit or Miss')
show_images(image, hit_or_missed_image, 'Original Image', 'Hit or Miss')
