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