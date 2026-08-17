import numpy as np

#Dealing with Missing Values

#np.nan -> not a number
arr=np.array([1,8,9,np.nan,2,6])
print(arr)

#np.inf and -np.inf -> positive and negative Infinite

a=np.array([np.inf,56,23,np.inf,np.nan])
print(a)

c=np.arange(1,10)
#special function for this

print(np.isnan(arr).any())

print(np.isinf(a).any())  

print(np.isfinite(c).any())

#removing nan and infinite value

new=np.nan_to_num(a)
print(new)