# Scalar Quantisation

import numpy as np
import imageio
import matplotlib.pyplot as plt

def get_codebook():
    codebook = {}
    for index in range(8):
        codebook.update({index: index * 32 + 12})
    return codebook

def compress(image):
    (row, col) = image.shape
    compressed_image = np.zeros(image.shape)
    for i in range(row):
        for j in range(col):
            index = image[i, j] / 32
            compressed_image[i, j] = index
    return compressed_image

def decompress(compressed_image):
    reconstructed_image = np.zeros(compressed_image.shape)
    (row, col) = compressed_image.shape
    codebook = get_codebook()
    for i in range(row):
        for j in range(col):
            reconstructed_image[i, j] = codebook[compressed_image[i, j]]
    return reconstructed_image

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

if __name__ == '__main__':
    image = imageio.imread('lena.jpg')
    compressed_image = compress(image)
    decompressed_image = decompress(compressed_image)
    show_images(image, compressed_image, 'Original Image', 'Compressed Image')


