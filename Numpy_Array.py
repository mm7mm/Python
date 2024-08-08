import numpy as np

# Create a 1-dimensional numpy array with elements "a", "b", "c", "d", "e"
a = np.array(["a", "b", "c", "d", "e"])

print(a.ndim)  # Print the number of dimensions of array 'a' (1 dimension)
print(a[1])    # Print the element at index 1 in array 'a' ("b")
print(a[::3])  # Print elements from array 'a' starting at index 0 with a step of 3 ("a", "d")

print("==========================")

# Create a 2-dimensional numpy array
b = np.array([
    ["b", "c", "d"],
    ['a', 'b', 'c'],
    ['h', 'i', 'j']
])

print(b.ndim)  # Print the number of dimensions of array 'b' (2 dimensions)
print(b[1][1]) # Print the element at row index 1 and column index 1 in array 'b' ("b")
print(b[:2, :1]) # Print the first two rows and the first column of array 'b'
# Output:
# [['b']
#  ['a']]

print("================================================")
print(b[::2, ::2]) # Print elements from array 'b' with a step of 2 in both dimensions
# Output:
# [['b' 'd']
#  ['h' 'j']]
 