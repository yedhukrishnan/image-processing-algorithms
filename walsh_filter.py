# Walsh Transform

import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.misc as misc

def binary(number, m):
    binary_string = bin(number)[2:]
    binary_string = '0' * (m - len(binary_string)) + binary_string
    return [int(i) for i in list(binary_string)]

def walsh(N):
    walsh_transform = np.zeros((N, N))
    m = int(math.log(N, 2))
    for n in range(N):
        for k in range(N):
            bin_n = binary(n, m)
            bin_k = binary(k, m)
            result = 1.0 / N
            for i in range(m):
                result = result * ((-1) ** (bin_n[i] * bin_k[m - 1 - i]))
            walsh_transform[n, k] = result
    return walsh_transform

def show_images(image1, image2, image3, image4, title1, title2, title3, title4):
    f, a = plt.subplots(2, 2)
    a[0, 0].imshow(image1, cmap='gray')
    a[0, 0].set_title(title1)
    a[0, 1].imshow(image2, cmap='gray')
    a[0, 1].set_title(title2)
    a[1, 0].imshow(image3, cmap='gray')
    a[1, 0].set_title(title3)
    a[1, 1].imshow(image4, cmap='gray')
    a[1, 1].set_title(title4)
    plt.show()

image = misc.imread('lena.jpg')
# We are assuming the image is a square image
# and generating a kernel of that order
n = image.shape[0]
kernel = walsh(n)

# Find the image transformed to frequency domain
transformed_image = np.dot(np.dot(kernel, image), kernel.T)

# Find the inverse of the image
inversed_image = (1.0 / n) * np.dot(np.dot(kernel, transformed_image), kernel.T)

show_images(image, kernel, transformed_image, inversed_image, 'Image', 'Kernel', 'Walsh Transformed Image', 'Inversed Image')
