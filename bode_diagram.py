# dit is de verkeerde !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ff goede uploaden
#============================================================

import numpy as np

# array
arr = np.array([2e-9, 5e-9, 10e-9, 20e-9, 50e-9, 100e-9, 200e-9,500e-9,1e-6,2e-6,5e-6,10e-6,20e-6,50e-6,100e-6,200e-6,500e-6,1e-3,2e-3,5e-3,10e-3,20e-3,50e-3,100e-3,200e-3,500e-3,1,2,5,1020,50,100])
print("Array is : ", arr)

# element to which nearest value is to be found
x = (1/300)*3
print("Value to which nearest element is to be found: ", x)

# calculate the difference array
difference_array = np.absolute(arr-x)

# find the index of minimum element from the array
index = difference_array.argmin()
print("Nearest element to the given values is : ", arr[index])
print("Index of nearest value is : ", index)
