import numpy as np
import matplotlib.pyplot as plt
import imageio

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1)
    a[0].set_title(title1)
    a[1].imshow(image2)
    a[1].set_title(title2)
    plt.show()

def rgb_to_hsi(image):
    # Separate image into RGB components
    R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]

    # Calculate the difference for finding cos inverse
    dRG, dRB, dGB = R - G, R - B, G - B
    cos = (dRG + dRB) / (2 * np.sqrt(dRG ** 2 + dRB * dGB))
    H = np.arccos(cos)

    # If any value is NaN (Not a Number, this happens 
    # while we divide by zero), change it back to 0
    H[np.isnan(H)] = 0.0

    # Calculate I
    I = image.mean(axis = 2)
    Imin = image.min(axis = 2)
    I[I == 0.0] = 1

    # S part
    S = 1 - Imin / I

    # Put the HSI components into a single image and return
    hsi_image = np.zeros(image.shape)
    hsi_image[:, :, 0] = H
    hsi_image[:, :, 1] = S
    hsi_image[:, :, 2] = I

    return hsi_image

image = imageio.imread('kid.jpg')
show_images(image, rgb_to_hsi(image), 'RGB', 'HSI')
