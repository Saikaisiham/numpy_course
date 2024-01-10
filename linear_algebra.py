import numpy as np 


a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)
result = np.matmul(a, b)
print(result)


#Find the determinant
c = np.identity(7)
print(np.linalg.det(c))


#Statistics


stat_array = np.array([[1,2,3],[4,5,6]])
print(np.min(stat_array))
print(np.max(stat_array))