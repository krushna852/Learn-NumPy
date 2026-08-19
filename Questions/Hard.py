import numpy as np

#1.Use boolean indexing to filter values less than a 30 number

arr = np.array([5, 12, 29, 30, 44, 7, 18])

new=arr[arr<30]
idx=np.where(arr<30)
b=arr[idx]
print(b)
print(new)

#2.Count the number of occurrences of each unique element

arr = np.array([2, 3, 2, 5, 3, 3, 2, 5])
values , count =np.unique(arr,return_counts=True)

freq=dict(zip(values,count))
print(freq)

#3Find the intersection and union of two arrays
a = np.array([1, 2, 3, 5, 7])
b = np.array([3, 4, 5, 6, 7])

inter=np.intersect1d(a,b)
uni=np.union1d(a,b)
print(inter)
print(uni)

#4. Transpose a matrix

a=np.arange(21,30).reshape(3,3)
print(a.transpose())

#5.Compute the eigenvalues and eigenvectors of a matrix

a=np.array([[4,2],[1,3]])
eigval , eigvec = np.linalg.eig(a)
print(eigval)
print(eigvec)

#6.Solve a linear equation
#given  x + 2y = 8 and 3x + 4y = 18.

#ax=b

a=np.array([[1,2],[3,4]])
b=np.array([8,18])

sol=np.linalg.solve(a,b)
print(sol)

#7.Create an 8×8 checkerboard pattern using 0s and 1s

arr=np.zeros([8,8]).astype(np.int64)
arr[1::2,::2]=1
arr[::2,1::2]=1
print(arr)

#8.Find nearest value of 3
arr = np.array([1.5, 2.8, 3.2, 4.1])
arr=arr[arr<=3]
print(arr[-1])

#9.Convert to object array
arr = np.array([1, 'a', 3, 4, 5]) 

obj_arr = np.empty(arr.size, dtype='object')

obj_arr[:] = arr

obj_arr[1] = 'a'
print(obj_arr)
print(obj_arr.dtype)
arr=arr.astype(str)
print(arr)
print(arr.dtype)

#10.Compute the mean, median, and standard deviation of a NumPy array

arr = np.array([10, 20, 30, 100, 200, 300])

print(arr.mean())
print(arr.var())
print(arr.std())
