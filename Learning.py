#Array Reshaping

import numpy as np

a=np.arange(1,7)
re=a.reshape(2,3)
print(re)

re2=re.reshape(3,2)
print(re2)


# ravel -> convert to 1D array

re3=re2.ravel()
print(re3)

# flatten -> convert to 1D array
re4=re2.flatten()
print(re4)

#Differnce Between ravel And flatten

re4[0]=5
print(re2) # flatten returns a copy of an array so changes not reflect in main array
print(re4)



re3[0]=5
print(re2) # ravel returns a view of an array changes it that array changes into main array
print(re3)
