import numpy as np 

#Multidimensoinal Slicing

matrix=np.arange(1,10).reshape(3,3)
print(matrix)

print(matrix[0:2 , 0:3])  # [rows (start:end:step) , columns (start:end:step)]
print(matrix[1: , :])

print(matrix[1,1:3])

print(matrix[1:3, 1:3])

