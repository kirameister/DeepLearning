#!/usr/bin/env python

import numpy as np

A = np.array([1,2,3,4])

# show the content
print(A) # [1 2 3 4]

# show the number of dimentions of given array 
np.ndim(A) # 1

# show the shpaes (size) of the given array for all the dimentions
A.shape    # (4,)
# show the shpaes (size) of the given array for given dimentions
A.shape[0] # 4

B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B) # 2
B.shape    # (3, 2)


## Inner product
A = np.array([1,2,3,4]).reshape(2,2)
B = np.array([5,6,7,8]).reshape(2,2)
AB = np.dot(A,B) # note that result would be different from np.dot(B,A)
print(AB)

A2 = np.array([1,2,3,4,5,6]).reshape(2,3)
B2 = np.array([1,2,3,4,5,6]).reshape(3,2)
AB2 = np.dot(A2,B2) # note that result would be different from np.dot(B,A)
print(AB2)


