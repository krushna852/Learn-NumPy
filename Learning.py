import numpy as np

#Transpose Of Matrix

arr=np.arange(1,10).reshape(3,3)
print(arr)

print(arr.transpose())

#Swapaxes :- swap 2 specific axes

arr=np.array([[[1,5,6],[5,9,6]]])
print(arr)
print(arr.shape)  # (1,2,3) swap 0th axes with 1st 1 <-> 2

swap=np.swapaxes(arr,0,1)
print(swap.shape)
print(swap)
