import numpy as np 


a = np.array([[1,2,3,4,5,6,7],
              [8,9,10,11,12,13,14]])
print(a)


#get a specific element[r, c ]
print(a[1, -2])
print(a[1, 5])


#get a specific row
print(a[0, 5:])

#get a specific column
print(a[:, 2])

#Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:-1:2])

#replace
a[1,6] = 8
print(a)
a[:,2] = 5
print(a)
a[:,1] = [2001,2008]
print(a)

