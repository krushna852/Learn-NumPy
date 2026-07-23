import numpy as np


#Index Arrays

#1. np.take ( array , list of index)

a=np.arange(1,11)
ind=[0,5]
print(np.take(a,ind))

#Iterating with np.nditer : for looping through array
arr=np.array([[1,2],[2,3]])

for i in np.nditer(arr):
    print(i,end=" ")
print("\n")
#Iterating with ndenumerate : it returns both index and value

for ind , i in np.ndenumerate(arr):
    print(ind,i)