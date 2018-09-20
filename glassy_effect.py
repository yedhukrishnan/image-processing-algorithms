# Glassy effect

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc
import random

def glassy(image):
    (row, col) = image.shape
    # Define the mask size
    m = 3
    n = 3
    # Empty array to store the glassy effect image
    glassy = np.zeros(image.shape)
    for i in range(row):
        for j in range(col):
            # Define the mask
            mask = image[i:i + m, j:j + n]
            # Select a random pixel from the mask and
            # assign it to the current pixel position
            random_pixel = random.sample(mask.flatten(), 1)[0]
            glassy[i, j] = random_pixel
    return glassy

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

img = misc.imread('gray_sign.jpg')

show_images(img, glassy(img), 'Original Image', 'Glassy Effect Image')
