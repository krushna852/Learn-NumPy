import numpy as np

#comulative Operations -> running oprtsions

arr=np.array([1,2,3])

print(np.cumsum(arr))

print(np.cumprod(arr)) 

#Conditional Based Choices 

choice=np.where(arr%2==0,"even","odd")
print(choice)

a=np.arange(1,11)
print(np.argwhere(a%2==0))  # It returns index of element

result=np.logical_and(a<5,a%2==0)
print(result) # it returns True and False

#for 2D Array

matrix=np.arange(1,10).reshape(3,3)
print(np.argwhere(matrix<5))
print(np.where(matrix%2==0,-1,0))

res=np.logical_and(matrix%2==0, matrix > 3)
print(matrix[res])

res=np.logical_or(matrix !=4,matrix<4)
print(matrix[res])