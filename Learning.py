import numpy as np

#Concatination

a=np.array([1,2])
b=np.array([3,4])

c=np.concatenate((a,b))
print(c)

#Using vstack :-  vertical stacking (concatinate by adding rows)

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(np.vstack((arr1,arr2)))

#Using hstack :- horizontal stacking (concatinate by adding columns)

print(np.hstack((arr1,arr2)))

#Only stack

print(np.stack((arr1,arr2),axis=0)) # 0 -> rows ,1-> columns
