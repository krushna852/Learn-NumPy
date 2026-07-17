import numpy as np

li=[1,2,3,4,5,6]
print(np.array(li))

a=np.arange(10,1,-1) # start stop step
print(a)

b=np.linspace(0,1,3) # (start,ending, n-> is n numbers between  start and end)
print(b)

c=np.logspace(1,3,2) #logrithmetic scale 10^1,10^2,10^3 from this only 2 
print(c)

d=np.zeros(4) # create a array of zeroes
print(d)

#Matrix Using Array
e=np.zeros([2,3])
print(e)


#Array of ones
a=np.ones([3,4],dtype=str)
print(a)

#array of Any one Random Number
b=np.full(5,7) # (number of value, value)
print(b)

b=np.full([5,3],9) # (pass Dimension [rows , columns] , Value)
print(b)

#Empty Array
a=np.empty([2,3]) #([row , cloums])
print(a)