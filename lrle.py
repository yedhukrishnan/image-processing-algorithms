# Run-Length Encoding
import numpy as np
import imageio
from matplotlib import pyplot as plt

# Function to encode image with RLE
def encode(image):
    encoded_string = ''
    (rows, cols) = image.shape
    for i in range(rows):
        encoded_row = ''
        # Keep the first pixel as the previous pixel
        previous_pixel = image[i, 0]
        count = 1
        # Start loop from the next pixel
        for j in range(1, cols):
            current_pixel = image[i, j]
            if previous_pixel == current_pixel:
                count += 1
            else:
                # If current pixel is different, encode the previous pixel
                # with count. Set the current pixel as next previous pixel
                # and reset count to 1
                string = str(previous_pixel) + '@' + str(count) + ' '
                encoded_row = encoded_row + string
                previous_pixel = current_pixel
                count = 1
            # If it is the last pixel, encode it
            if j == cols - 1:
                string = str(previous_pixel) + '@' + str(count) + ' '
                encoded_row = encoded_row + string
        # Append new line to the encoded string
        encoded_string += encoded_row + '\n'

    return encoded_string

# Function to decode the RLE encoded image from encoded string
def decode(string):
    encoded_rows = string.split('\n')

    # Number of rows = Number of lines in the encoded string
    rows = len(encoded_rows)

    # Number of columns = Sum of all the counts in one row
    encoded_row = encoded_rows[0].split()
    count = 0
    for encoded in encoded_row:
        print(encoded)
        count += int(encoded.split('@')[1])

    cols = count

    image = np.zeros((rows, cols))
    for i, encoded_row in enumerate(encoded_rows):
        encoded_row = encoded_row.split()
        j = 0
        for string in encoded_row:
            pixel = int(string.split('@')[0])
            count = int(string.split('@')[1])
            for k in range(count):
                image[i, j] = pixel
                j += 1
    return image



image = imageio.imread('les_binary.jpg')

# Encode the image
encoded = encode(image)
print(encoded)

# Decode the image
decoded_image = decode(encoded)
plt.imshow(decoded_image, cmap='gray')
plt.show()
