# Gray Level Slicing by preserving background

import numpy as np
import scipy.misc as misc
import matplotlib.pyplot as plt

def grayslicing(image, a, b):
    (rows, cols) = image.shape
    graysliced_image = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            # If the pixel value is within the range, then set the value as 255
            # Otherwise set it to the actual pixel value
            if a <= image[i,j] <= b:
                graysliced_image[i,j] = 255
            else:
                graysliced_image[i,j] = image[i, j]

    return graysliced_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

image = misc.imread('gray_nature.jpg')

# Input the range values
a = input("value of a =  ")
b = input("value of b = ")

sliced_image = grayslicing(image, a, b)
show_images(image, sliced_image, 'Original Image', 'Gray Level Sliced Image (preserving background)')
