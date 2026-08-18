import numpy as np

#1.Compute the mean, median, and standard deviation of a NumPy array

arr=np.array([10,20,30,100,200,300])

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.var(arr))
print(np.std(arr))

#2.Remove common items from 2 array

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

c=np.isin(a,b)
print(a[~c])

#3.Normalize a NumPy array (values between 0 and 1)

a=np.array([10,20,30,40,50])

print(np.linspace(0,1,len(a)))

#4.Get the positions where elements of array a and b match

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 4, 3, 7, 8])

print(np.argwhere(a==b))

#5.Extract numbers from an array
#Write a code to extract all numbers from an array that are between 5 and 10 (inclusive).

a=np.arange(15)
cond=np.logical_and(a<11,a>4)
print(a[cond])

#6.Create a random 3×2 matrix and find its maximum and minimum values

import random

a=np.random.rand(2,3)
print(a)
print(np.max(a))
print(np.min(a))

#7.Sorting a NumPy array based on a specific column

a = np.array([[1, 100, 100], [0, 5, 6], [2, 70, 1]])

temp = a[:,1].argsort()

print(a)
print(a[temp])

#8.Delete and Insert a Column in a NumPy Array


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumnToAdd = np.array([10, 10, 10])
print(sampleArray)
sampleArray=np.delete(sampleArray,1,axis=1)
new=np.insert(sampleArray,1,newColumnToAdd,axis=1)
print(new)

#9.Swap column 1 and 2 in a 2D array

a=np.arange(9).reshape(3,3)
print(a)

a[:,[0,2]]=a[:,[2,0]]
print(a)

#10. Generate 10 random integers between 1 and 100

a=np.random.randint(1,101,size=10)
print(a)

#11.Create a 3×3 array of random integers and sort it row-wise

a=np.random.randint(1,100,size=[3,3])
print(a)
a=np.sort(a,axis=0)
print(a)

#12.Shuffle an array randomly

np.random.shuffle(a)
print(a)

#13.Create a 5×5 2D array with 1s on the border and 0s inside.

z=np.zeros([5,5])
z[0]=1
z[:,0]=1
z[:,-1]=1
z[-1]=1
print(z)
z=np.ones([5,5])
z[1:-1,1:-1]=0
print(z)

#14.Check if an array contains any NaN values.

a = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(a).any())

#15.Sort the rows of a 2D array based on the values of the second column

arr = np.array([[8, 11, 1],
                [5, 2, 7],
                [6, 9, 3]])

sorted=arr[:,1].argsort()
print(arr[sorted])

#16 Insert Elements in an Array


a=np.arange(1,11).astype(np.float64)
b=np.insert(a,[3,5],[np.nan,np.inf])
print(b)
b=np.logical_or(np.isnan(b).any(),np.isinf(b).any())
print(b)


#17.Flatten a multi-dimensional NumPy array

a=np.arange(1,10).reshape(3,3)
new = a.flatten()
print(new)

#18.Stack two arrays vertically and horizontally

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c=np.vstack((a,b))
print(c)

c=np.hstack((a,b))
print(c)

#19.Split an array into 3 equal parts

a=np.arange(1,13)
print(np.split(a,3))

a=np.arange(1,10).reshape(3,3)
print(np.hsplit(a,3))

#20.Perform Addition and Squaring on Arrays

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

add=arrayOne+arrayTwo
print(add)

square=add**2
print(square)

#21.Invert a matrix

matrix=np.array([2,9,9,6,5,3,7,8,99]).reshape(3,3)
print(matrix)
inv_matrix=np.linalg.inv(matrix)
print(inv_matrix)