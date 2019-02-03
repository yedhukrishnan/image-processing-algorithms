# Color image histogram

import numpy as np
from matplotlib import pyplot as plt
from scipy import misc

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1)
    a[0].set_title(title1)
    a[1].imshow(image2)
    a[1].set_title(title2)
    plt.show()

def get_count(image):
	(row,col)=image.shape
	count=np.zeros(256)
	for i in range(row):
		for j in range(col):
			pixel = image[i,j]
			count[pixel] += 1
	return count

# Load the  rgb image
rgb_image = misc.imread('kid.jpg')
(row,col,_)=rgb_image.shape


# Separate RGB into components
R = rgb_image[:, :, 0]
G = rgb_image[:, :, 1]
B = rgb_image[:, :, 2]

count_r=get_count(R)
count_g=get_count(G)
count_b=get_count(B)

f, a = plt.subplots(1, 2)
a[0].imshow(rgb_image)
a[0].set_title('Image')
a[1].set_title('Histogram')
a[1].plot(range(256),count_r,'r')
a[1].plot(range(256),count_g,'g')
a[1].plot(range(256),count_b,'b')
plt.show()
