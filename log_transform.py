# Logarithmic tranformation

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import math

def logarithmic_transform(image, c):
    (row, col) = image.shape
    new_image = np.zeros(image.shape)
    for i in range(row):
        for j in range(col):
            # Find the log of pixel value
            new_image[i, j] = c * math.log(image[i, j] + 1, 2)
            if new_image[i, j] < 0:
                new_image[i, j] = 0
            elif new_image[i, j] > 255:
                new_image[i, j] = 255
    return new_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

image = misc.imread('gray_sign.jpg')
c = input('Enter c value : ')
log_image = logarithmic_transform(image, c)
show_images(image, log_image, 'Original Image', 'Logarithmic Transformed Image')
