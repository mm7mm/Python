import numpy as np
import time
import sys

print("==========================")
elements = 180
my_list = range(elements)
# The elements in my_list are not printed because the code for printing is commented out
for n in my_list:
    print(n)
print("==========================") 
# Arrays are not created, and time is not measured because the code is commented out
my_array = np.arange(elements)
my_array2 = np.arange(elements)
list_start = time.time()

# Calculate the sum of elements using zip and record the time
list_result = [(n1 + n2) for n1, n2 in zip(my_array, my_array2)]
print(f"List Time : {time.time() - list_start}")

print("==========================")
# The time for numpy array operations is not measured because the code is commented out
array_start = time.time()
array_result = my_array + my_array2
print(f"Array Time : {time.time() - array_start}")
for n1, n2 in zip(my_array, my_array2):
    print(n1 + n2)
print("==========================")
my_array = np.arange(100)
print(my_array)  # Prints elements from 0 to 99
print(my_array.itemsize)  # Size of each element in the array (usually 8 bytes for float)
print(my_array.size)  # Number of elements in the array (100 elements)
print(f"All Bytes : {my_array.itemsize * my_array.size} ")
# Calculate the total size of the array (number of elements × size of each element)

print("==========================")
my_list = range(100)
print(sys.getsizeof(my_list[1]))  # Size of a single element (usually 28 bytes for an integer)
print(len(my_list))  # Number of elements in the list (100 elements)
print(f"All Bytes : {sys.getsizeof(1) * len(my_list)}")
# Calculate the total size of the list (number of elements × size of each element)
