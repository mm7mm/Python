import numpy as np
import time
import sys

elements =180
my_list=range(elements)
# for n in my_list:
#     print(n)
    
my_array =np.arange(elements)
my_array2 =np.arange(elements)
list_start=time.time()
list_result =[(n1+n2)  for n1,n2 in zip(my_array,my_array2)]


array_start=time.time()
array_result = my_array +my_array2
# for n1 ,n2 in zip(my_array,my_array2):
#     print(n1+n2)