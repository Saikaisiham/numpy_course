import numpy as np
from script1 import a

# All 0s Matrix
zero_array = np.zeros((2, 3))
print(zero_array)

# All 1s Matrix
one_array = np.ones((2, 3), dtype='int32')
print(one_array)
print(one_array.itemsize)

# Any other number
number_array = np.full((2, 2), 88.5, dtype='float32')
print(number_array)

# Any other number(full_like)
test_array = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])


