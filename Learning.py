import numpy as np


#Views vs Copies

#View :-
arr=np.array([1,2,3,4,5,6])
view=arr[1:4]
print(view)

view[1]= 4
print(view)
print(arr) #changes in view aslo reflect in orignal array

#Copy :-

cop=arr[1:4].copy()
cop[1]=3
print(cop)
print(arr) # Changes Not affect orignal array