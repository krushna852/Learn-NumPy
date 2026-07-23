import numpy as np 

#Indexing And Slicing

arr=np.arange(1,7)

print(arr[0]) # +ve indexing
print(arr[2])

print(arr[-1])  # -ve indexing
print(arr[-3])

#slicing
print(arr[0:4]) #start : end (explicit) : step
print(arr[::-1]) # reverse a array

print(arr[-4:-1])
print(arr[-1:-4:-1])