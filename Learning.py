import numpy as np

#Broadcasting

image=np.array([[150,950],[400,250]])
brightness=image+50 #here 50 is consider as (2,2) array with all value 50
print(brightness)

a=np.array([[1],[2],[3]])
b=np.array([1,2,3])
print(a*b)