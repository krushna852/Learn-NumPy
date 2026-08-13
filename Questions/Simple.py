import numpy as np

#1. Create a 1D NumPy array of numbers from 0 to 9

arr=np.arange(10)
print(arr)

#2.Convert 1D array to 2D
a=arr.reshape(2,5)
print(a)

#3.Print Array Attributes Shape,Dimensions and Size of each items
print(a.shape)
print(a.ndim)
print(a.itemsize)

#4.Create a 3×3 NumPy array of all True

arr1=np.full([3,3],True)
print(arr1)

#5 Extract the documentation of NumPy’s arange() function

print(np.info(np.arange))

#6.Create a 1D array filled with zeros and another filled with ones

a1=np.ones([3,3],dtype=int)
print(a1)

a2=np.zeros([2,3],dtype=int)
print(a2)

#7.Create a 1D array of 10 evenly spaced values between 5 and 50

b=np.linspace(5,50,10).astype(np.int64)
print(b)

#8. Convert a Python list into a NumPy array
li=[1,2,3,4,56,8,9,5,7,8,6,2]
print(np.array(li))

#9.Find the memory size of a NumPy array of numbers from 0 to 9

print(b.nbytes)

#10.Reverse a 1D NumPy array

a=np.array(li)
print(a)
print(a[::-1])