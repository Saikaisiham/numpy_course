import numpy as np 

a = np.array([1,2,3], dtype='int8')
print(a)

b = np.array([[5,6,7,8,9],[10,11,12,13,14]])
print(b)


#get Dimension 
print(a.ndim)
print(b.ndim)

#get Shape 
print(a.shape)#r, c
print(b.shape)

#get Type 
print(a.dtype)
print(b.dtype)

#get Size
print(a.itemsize)#bytes
print(b.itemsize)

#get Totalsize 
print(a.size)
print(a.size * a.itemsize)
print(a.nbytes)