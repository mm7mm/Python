import numpy as np

my_array = np.array([1, 2, 3])
my_array2 = np.array([1.2, 2.3 ,4.5])
my_array3 = np.array(['MO', 'ahmed', 'mostafa'])

print(my_array.dtype)
print(my_array2.dtype)
print(my_array3.dtype)


print("============================")
my_array4 = np.array([1, 2, 3] ,dtype='f')
my_array5 = np.array([1.2, 2.3 ,4.5] ,dtype='i')
# my_array6 = np.array(['MO', 'ahmed', 'mostafa'], dtype="int") # Value error

print(my_array4.dtype)
print(my_array5.dtype)
# print(my_array6.dtype)


print("============================")
#Change Data Type Of Existing Array
my_array7 = np.array([1, 0, 3, 4, 5, 6])
print(my_array7.dtype)
print(my_array7) 
my_array7=my_array7.astype('float')
print(my_array7.dtype)



print("============================")
my_array7=my_array7.astype('bool')
print(my_array7.dtype)
print(my_array7)

print("============================")
#Test Capacity


# Create a numpy array with specified elements and dtype as 'f' (float32)
my_array8 = np.array([100, 200, 300, 400, 500], dtype='f')

print(my_array8.dtype)  #float32   
print(my_array8.itemsize)  


my_array8 = my_array8.astype('float')

print(my_array8.dtype)     #float64

