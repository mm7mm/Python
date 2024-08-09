import numpy as np

my_array1 = np.array([1, 2, 3, 4])
print(my_array1.ndim)  # Output: 1
print(my_array1.shape)  # Output: (4,)

print("="*30)

my_array2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]])
print(my_array2.ndim)  # Output: 2
print(my_array2.shape)  # Output: (3, 4)

print("="*30)

my_array3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13], [15, 16, 17, 18]]])
print(my_array3.ndim)  # Output: 3
print(my_array3.shape)  # Output: (1, 4, 4)

print("="*30)

my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)  # Output: 1
print(my_array4.shape)  # Output: (12,)

reshaped_array4 = my_array4.reshape(3, 4)
print(reshaped_array4.ndim)  # Output: 2
print(reshaped_array4.shape)  # Output: (3, 4)
print(reshaped_array4)
# Output:
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print("="*30)

my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(my_array5.ndim)  # Output: 2
print(my_array5.shape)  # Output: (2, 10)

print("="*30)

reshaped_array5 = my_array5.reshape(2, 5, 2)
print(reshaped_array5.ndim)  # Output: 3
print(reshaped_array5.shape)  # Output: (2, 5, 2)
print(reshaped_array5)
# Output:
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]
#   [ 7  8]
#   [ 9 10]]

#  [[ 1  2]
#   [ 3  4]
#   [ 5  6]
#   [ 7  8]
#   [ 9 10]]]
