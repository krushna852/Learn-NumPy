import numpy as np
import sys

a=[1,2,3,4,5,6,7,8,9,10]
b=np.array(a)
print("size of list is", sys.getsizeof(a))
print("size of array is", b.nbytes)