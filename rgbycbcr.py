# RGB to YCbCr

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

def convert_to_ycbcr(rbg_image):
	# Separate RGB into components
	R = rgb_image[:, :, 0]
	G = rgb_image[:, :, 1]
	B = rgb_image[:, :, 2]

	# Calculate Y Cb Cr values
	Y = (77 / 256.0) * R + (150 / 256.0) * G + (29 / 256.0) * B
	Cb = -(44 / 256.0) * R - (87 / 256.0) * G + (131 / 256.0) * B + 128
	Cr = (131 / 256.0) * R - (110 / 256.0) * G - (21 / 256.0) * B + 128

	# Combine Y Cb Cr values into a single image
	ycbcr_image = np.zeros(rgb_image.shape)
	ycbcr_image[:, :, 0] = Y
	ycbcr_image[:, :, 1] = Cb
	ycbcr_image[:, :, 2] = Cr

	# Return the float image as int image
	return ycbcr_image.astype(np.uint8)


rgb_image = imageio.imread('kid.jpg')
ycbcr_image = convert_to_ycbcr(rgb_image)

show_images(rgb_image.astype(np.uint8), ycbcr_image, 'RGB', 'YCbCr')

