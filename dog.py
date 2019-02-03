# Difference of Gaussian

from skimage import data, feature, color, img_as_float
from matplotlib import pyplot as plt
import scipy.ndimage.filters as filters
from scipy import misc

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()


def difference_of_gaussian(image):
	k = 1.6
	sigma = 8.0
	s1 = filters.gaussian_filter(image, k * sigma)
	s2 = filters.gaussian_filter(image, sigma)
	dog = s1 - s2
	return dog


img = misc.imread('lena.jpg')
dog = difference_of_gaussian(img)
show_images(img, dog, 'Image', 'DoG')
