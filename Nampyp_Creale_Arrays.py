import numpy as np

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(my_array)
print(my_list)
print("========================")

# Accessing Elements
print(my_array[0])
print(my_list[0])

print("========================")

a = np.array(10)
b = np.array([19, 12])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[11, 2, 3], [5, 6, 5]]])

print(d[1][1])
print("========================")
#Number of Dimensions
print(a.ndim)
print(d.ndim)

print("========================")
#Custom Dimension
my_custom_array = np.array([1,2,3] , ndmin=3)
print(my_custom_array)
print(my_custom_array.ndim)

print("========================")

print(id(my_list[0]))
print(id(my_list[1]))

print(id(my_array[0]))
print(id(my_array[1]))

print("========================")
my_list_of_data= [1,2,3,4,5,6,"a","b",True ,10.5]
my_array_of_data=np.array([1,2,3,4,5,6,"a","b",True ,10.5])

print(my_list_of_data)
print(my_array_of_data)
print("=========================)")
print(type(my_list_of_data[0]))  #==>integer
print(type(my_array_of_data[0])) #==>string


print("==========================")

my_list_of_data_tow= [1,2,3,4,5,6,"a","b",True ,10.5]
my_array_of_data_tow=np.array([1,2,3 ,10.5]) #if "a" on array then ==>string

print(my_list_of_data_tow)
print(my_array_of_data_tow)
print("=========================)")
print(type(my_list_of_data_tow[0]))  #==>integer
print(type(my_array_of_data_tow[0])) #==>floating


print("==========================")