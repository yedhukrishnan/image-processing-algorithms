# RGB to YIQ

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

def convert_to_yiq(rbg_image):
	# Separate RGB into components
	R = rgb_image[:, :, 0]
	G = rgb_image[:, :, 1]
	B = rgb_image[:, :, 2]

	# Calculate YIQ values
	Y = np.round(0.299 * R + 0.587 * G + 0.114 * B)
	I = np.round(0.596 * R - 0.275 * G - 0.321 * B)
	Q = np.round(0.212 * R - 0.523 * G + 0.311 * B)

	# Combine YIQ values into a single image
	yiq_image = np.zeros(rgb_image.shape)
	yiq_image[:, :, 0] = Y
	yiq_image[:, :, 1] = I
	yiq_image[:, :, 2] = Q

	# Return the float image as int image
	return yiq_image.astype(np.uint8)


rgb_image = imageio.imread('kid.jpg')
yiq_image = convert_to_yiq(rgb_image)
show_images(rgb_image.astype(np.uint8), yiq_image, 'RGB', 'YIQ')

