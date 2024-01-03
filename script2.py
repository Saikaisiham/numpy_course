import numpy as np 


#3D 
a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

#get a specific element 
print(a[1,1,1])

#replace 
a[:,1,:] = [[6,6],[8,8]]
print(a)