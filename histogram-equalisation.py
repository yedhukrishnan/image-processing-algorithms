import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def equalize(image):
    (row, col) = image.shape

    # Find the count of each pixel
    pixel_count = np.zeros((256, 1))
    for pixel in image.flatten():
        pixel_count[pixel] += 1

    # Find the running sum by adding all the values upto that
    running_sum = np.zeros((256, 1))
    running_sum[0] = pixel_count[0]
    for i in range(1, 256):
        running_sum[i] = running_sum[i - 1] + pixel_count[i]

    # Calculate the new pixels by dividing the running sum
    # with total number of pixels and by multiplying it with
    # the largest pixel value.
    # Total number of pixels = row * col
    # Largest pixel value = 255
    new_pixels = np.round((running_sum / (row * col)) * 255)

    # Create the histogram equalised image with new pixel values
    new_image = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            new_image[i, j] = new_pixels[image[i, j]]

    return new_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

image = misc.imread('gray_sign.jpg')
histogram_equalized_image = equalize(image)
show_images(image, histogram_equalized_image, 'Original Image', 'Histogram Equalized Image')
