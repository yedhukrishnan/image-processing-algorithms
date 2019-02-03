# Kronecker product

import numpy as np

def kronecker(matrix1, matrix2):
    (row1, col1) = matrix1.shape
    (row2, col2) = matrix2.shape

    # Generate zero matrix to store the Kronecker product
    # The dimension will be (row1 * row2, col1 * col2)
    new_matrix = np.zeros((row1 * row2, col1 * col2))

    for i in range(row1):
        for j in range(col1):
            # Generate the multiplied matrix and add it as a subset of the Kronecker product
            new_matrix[i * row2:i * row2 + row2, j * col2: j * col2 + col2] = matrix2 * matrix1[i, j]

    return new_matrix

# Generate two matrices to find the Kronecker product
a = np.arange(9).reshape((3, 3))
b = np.ones((2, 2))

print 'Kronecker product of'
print a
print 'and'
print b
print 'is given as follows: '
print kronecker(a, b)
