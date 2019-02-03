# Color image filtering

import numpy as np
from matplotlib import pyplot as plt
from scipy import misc, signal


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
    a[0].imshow(image1)
    a[0].set_title(title1)
    a[1].imshow(image2)
    a[1].set_title(title2)
    plt.show()
# Load the  rgb image
rgb_image = misc.imread('kid.jpg')
(row,col,_)=rgb_image.shape
# Generate averaging filter
averaging_filter = np.ones((3, 3)) / 9.0

# Separate RGB into components
R = rgb_image[:, :, 0]
G = rgb_image[:, :, 1]
B = rgb_image[:, :, 2]

averaged_R = convolve(R, averaging_filter)
averaged_G = convolve(G, averaging_filter)
averaged_B = convolve(B, averaging_filter)


# Combine RGB values into a single image
averaged_image= np.zeros((row+2,col+2,3))
averaged_image[:, :, 0] = averaged_R
averaged_image[:, :, 1] = averaged_G
averaged_image[:, :, 2] = averaged_B


show_images(rgb_image,averaged_image.astype(np.uint8), 'RGB', 'Filtered Image')

