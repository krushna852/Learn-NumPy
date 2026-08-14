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

#11.Create a 3×3 identity matrix

I=np.eye(3).astype(np.int64)
print(I)

#12.Delete a Row or Column in a Matrix

a=np.arange(1,17).reshape(4,4)
print(a)

b=np.delete(a,[2],axis=0) #axis=0 to delete row
print(b)

c=np.delete(a,np.s_[0:2],axis=1) #axis =1 to delte column
print(c)

#13Create a 4×4 array and extract its first row and last column

print(a)
first_row=a[0]
print(first_row)

last_col=a[:,-1]
print(last_col)

#14.Extract Odd Rows and Even Columns

print(a)
odd_row=a[0::2]
print(odd_row)

even_col=a[:,1::2]
print(even_col)

sample=a[0::2,1::2]
print(sample)

#15.Stack arrays horizontally

s1=np.array([1,2,3])
s2=np.array([4,5,6])
s3=np.hstack((s1,s2))
print(s3)

#16.Slice the first two rows and first two columns from a 4×4 array

print(a)

result=a[0:2,0:2]
print(result)

#17.Replace all odd numbers in a NumPy array with -1

print(a)
for ind , i in np.ndenumerate(a):
    if i%2 == 1:
        a[ind]=-1
    else:
        pass


print(a)
a=np.arange(1,17).reshape(4,4)
a[a%2==1]=-1
print(a)


#18.Get the indices of non-zero elements in an array

arr=np.array([0,1,5,0,3,4,8,0,45,200,3,50,60,0,0,68,0]).astype(np.int64)

for ind , i in np.ndenumerate(arr):
    if i != 0:
        print(ind)
    else:
        pass

extra=np.nonzero(arr)
print(extra)

#19.Find the common items between two arrays
a = np.array([1, 2, 3, 2, 8, 4, 2, 4])
b = np.array([2, 4, 5, 6, 8])
print(np.intersect1d(a,b))

#20 Matrix multiplication

a=np.arange(1,7).reshape(2,3)
b=np.arange(1,7).reshape(3,2)

print(a@b)
print(np.dot(a,b))