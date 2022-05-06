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
print("arr1 -", arr1[::2, ::2])


