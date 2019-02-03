# Block Truncation Coding

import numpy as np
import matplotlib.pyplot as plt

# Function to find BTC of an image
def btc(image):
    (row, col) = image.shape
    # Find mean and variance (sigma)
    mean = image.mean()
    sigma = np.sqrt(image.var())
    # Change values which are greater than mean to 1
    # Change values which are less than mean to 0
    image[image > mean] = 1
    image[image != 1] = 0
    # Find the numer of ones in the new image
    q = image.sum()
    # Find the number of elements
    m = row * col
    # Find a and b
    a = np.round(mean - sigma * np.sqrt(q / (m - q)))
    b = np.round(mean + sigma * np.sqrt((m - q) / q))
    # Change all ones to b and all zeros to a
    image[image == 1] = b
    image[image == 0] = a
    return image

image = np.array([
        [65, 75, 80, 70],
        [75, 75, 82, 68],
        [84, 72, 62, 65],
        [66, 68, 72, 80]
    ])

print('Input: ')
print(image)
print('Output: ')
print(btc(image))


