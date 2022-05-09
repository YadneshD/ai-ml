import numpy as np
# tested on numpy==1.22.1
# https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
print("numpy=", np.__version__)

arr1 = np.random.randint(1,20, (3,4))
print("--------------------------INDEXING---------------------------")
print("arr1 =", arr1)
print("arr1[2,1], arr1[1,2] -", arr1[2,1], arr1[1,2])
print("arr1[:,2] -", arr1[:,2])
print("arr1[2,:] -", arr1[2,:])
print("arr1[:, :] -", arr1[:, :])
print("arr1[:2, 2:] -", arr1[:2, 2:])
print("arr1[:-2, -2:] -", arr1[:-2, -2:])
print("arr1[::2, ::2] -", arr1[::2, ::2])
print("access each individual element using indices", arr1[[0,1,2,2], [0,1,2,3]])
print("--------------------------AXIS---------------------------")
arr2 = np.random.randint(0, 10, (2,3,2))
print("arr2 =", arr2)
print("arr2.shape -", arr2.shape)
print("arr2.sum(axis=0) -", arr2.sum(axis=0))
print("arr2.sum(axis=1) -", arr2.sum(axis=1))
print("arr2.sum(axis=2) -", arr2.sum(axis=2))

