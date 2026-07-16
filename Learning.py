import time 
import numpy as np

start = time.time()
li=[1,2,3,4,5,6,7,8,9,10]*1000
li2=[]
for i in li:
    li2.append(i*2)
print("Total Time required is",time.time()-start)

new_start=time.time()
li1=[1,2,3,4,5,6,7,8,9,10]*1000
a=np.array(li1)
new_a=a*2
print("Total Time required is",time.time()-new_start)
