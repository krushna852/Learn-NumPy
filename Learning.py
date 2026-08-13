import numpy as np

#Remark np.info and .nbytes

a=np.arange(1,10)
print(a.nbytes) # it returns memory of an array
print(a.itemsize)

print(np.info(np.astype)) # it returns documentation or information 

# Spliting Of an Array

arr=np.arange(1,9)
print(np.split(arr,2)) # if equal divison

print(np.hsplit(arr,4)) # splits horizontally

a=np.arange(1,10).reshape(3,3)
print(np.vsplit(a,3))  # splits vertically only above 2 or 2d array