# Oil paint effect

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc

def oil_paint(image):
    (row, col) = image.shape
    # Define the small window size
    m = 5
    n = 5
    # Define an array to store the new matrix
    oil = np.zeros(image.shape)
    for i in range(row):
        for j in range(col):
            # Create subset of the matrix with given window size
            mask = image[i:i + m, j:j + n]
            # Reshape the 2D matrix into 1D array
            mask.reshape((mask.shape[0] * mask.shape[1], 1))
            # Define an array to store count
            h = np.zeros((256, 1))
            # Iterate through the pixels and increment count
            # For example if pixel is 40, h[40] += 1 (which is same as h[40] = h[40] + 1)
            for k in mask:
                h[k] += 1

            # Find the pixel with maximum count and assign it to new matrix
            oil[i, j] = np.argmax(h)
    return oil

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

img = misc.imread('gray_sign.jpg')
show_images(img, oil_paint(img), 'Original Image', 'Oil Painted Image')
