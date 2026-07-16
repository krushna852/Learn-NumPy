import time 

start = time.time()
i=1
li=[]
while i <=100000000:
    li=i
    i+=1
print("Total Time required is",time.time()-start)