# Laplacian of Gaussian

import scipy as sp
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import imageio

def show_images(image1, image2, title1, title2):
    f, a = plt.subplots(1, 2)
    a[0].imshow(image1, cmap='gray')
    a[0].set_title(title1)
    a[1].imshow(image2, cmap='gray')
    a[1].set_title(title2)
    plt.show()

image = imageio.imread('lena.jpg')
LoG = nd.gaussian_laplace(image, 2)
thres = np.absolute(LoG).mean() * 0.5
output = sp.zeros(LoG.shape)
w = output.shape[1]
h = output.shape[0]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        patch = LoG[y-1:y+2, x-1:x+2]
        p = LoG[y, x]
        maxP = patch.max()
        minP = patch.min()
        if (p > 0):
            zeroCross = True if minP < 0 else False
        else:
            zeroCross = True if maxP > 0 else False
        if ((maxP - minP) > thres) and zeroCross:
            output[y, x] = 1

show_images(image, output, 'Image', 'LoG')