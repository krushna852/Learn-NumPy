import numpy as np

a=np.full([5,2],15)
print(a)
print(a.ndim)

a=np.zeros([4,3])
print(a)
print(a.shape)

a=np.ones([3,2])
print(a)
print(a.size) # to check how many elements in an array

print(a.itemsize) # return size of each element