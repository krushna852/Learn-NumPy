import numpy as np

#Numpy Data Types and Type Casting

a=np.array([1,23,5,6,89])
print(a)
print(type(a))
print(type(a[2]))

a=np.array([23,12.26,47.02345,3.0254,50])
print(a)
print(type(a[1]))

a=np.array([True,False])
print(a)
print(type(a[1]))

a=np.array(["hfhf","apple","choclate","mango"])
print(a)
print(type(a[1]))

a=np.array([56,"hdvdb",56.12,True,"455"])
print(a)
print(type(a[1]))

#Type Casting
a=np.array([12,34,5,67])
a=a.astype(np.float64)
print(a)

b=np.array(["12","8","45","4"])
b=b.astype(np.int64)
print(b)

a=np.array([23.01,56.89,56.99,25.1,69.9999])
a=a.astype(np.str_)
print(a)

#type Casting Errors
a=np.array(["12","56.23","Hello","Welcom"])
a=a.astype(np.int64)
print(a) #error 