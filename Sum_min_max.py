import numpy as np
print("==============================")

my_array1 = np.array([10, 20, 30, 40, 50])
my_array2 = np.array([5, 15, 25, 35, 45])

print(my_array1 + my_array2)  # Output: [15 35 55 75 95]
print(my_array1 - my_array2)  # Output: [5 5 5 5 5]
print(my_array1 * my_array2)  # Output: [50 300 750 1400 2250]
print(my_array1 / my_array2)  # Output: [2. 1.33333333 1.2 1.14285714 1.11111111]

print("==============================")
my_array3 = np.array([[10, 20], [20, 30]])
my_array4 = np.array([[5, 40], [2, 5]])

print(my_array3 + my_array4)  # Output: [[15 60] [22 35]]
print(my_array3 - my_array4)  # Output: [[ 5 -20] [18  25]]
print(my_array3 * my_array4)  # Output: [[ 50 800] [ 40 150]]
print(my_array3 / my_array4)  # Output: [[ 2.  0.5] [10.  6.]]

print("==============================")
my_array6 = np.array([[10, 20], [20, 30]])
print(my_array6.min())  # Output: 10
print(my_array6.max())  # Output: 30
print(my_array6.sum())  # Output: 80

print("==============================")
my_array7 = np.array([[10, 20], [20, 30]])
print(my_array7.ravel())  # Output: [10 20 20 30]

my_array8 = np.array([[[10, 20], [20, 30], [30, 30], [1, 2]]])
print(my_array8.ndim)  # Output: 3
print(my_array8.ravel())  # Output: [10 20 20 30 30 30  1  2]
x = my_array8.ravel()
print(x.ndim)  # Output: 1
                   