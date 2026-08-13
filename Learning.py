import numpy as np

#Aggregate Functions

#For 1D Array

a=np.arange(1,10)

print(np.sum(a))

print(np.mean(a))

print(np.median(a))

print(np.var(a))

print(np.std(a))

print(np.min(a))

print(np.max(a))

#for 2D Array

a=a.reshape(3,3)

print(a)

print(np.sum(a,axis =0)) # sum of all elements in Single column

print(np.sum(a, axis=1)) #sum all elements in single row

print(np.min(a))