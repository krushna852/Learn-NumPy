import numpy as np


#Vectorization

def square(x):
    return x*x

squarev=np.vectorize(square)  # it Convert normsl function into numpy function

a=np.array([1,2,3,4,5,6])
print(squarev(a))