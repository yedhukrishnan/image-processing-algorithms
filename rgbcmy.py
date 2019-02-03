# RGB to CMY

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1)
    a[0].set_title(title1)
    a[1].imshow(image2)
    a[1].set_title(title2)
    plt.show()

rgb_image = misc.imread('kid.jpg')
cmy_image = 255 - rgb_image


show_images(rgb_image, cmy_image, 'RGB', 'CMY')
