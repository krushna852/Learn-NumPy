import numpy as np


def Matrix_multi(a,b):
    if a.shape[1] == b.shape[0]:
        li=[]
        i=0
        while i< a.shape[0]: #i is less than no of rows in frist array
            temp=0
            j=0
            z=0
            while j < a.shape[1] and z < b.shape[1]: #j < no of cloumns in 1st array or no of rows in 2nd array 
                temp=temp+(a[i][j] *b[j][z] )
                if j==(a.shape[1] - 1) and z < b.shape[1] : # z < no of coluns in 2nd array
                    li.append(temp)
                    temp=0
                    j=0
                    z+=1
                else:
                    j+=1
            i+=1
        return np.array(li).reshape(a.shape[0],b.shape[1])
    else:
        return "Multiplication is not possible"


a=np.arange(1,7)
a1=a.flatten().reshape(2,3)
a2=a.flatten().reshape(3,2)
result=Matrix_multi(a2,a1)
print(result)


c=np.arange(1,16).reshape(5,3)
d=np.arange(1,13).reshape(3,4)
result=Matrix_multi(c,d)
print(result)
