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
print("--------------------------AXIS SUM 3D ARRAY---------------------------")
arr3 = np.random.randint(0, 10, (2,3,2))
print("arr3 =[[", arr3[0,0], arr3[0,1], arr3[0,2], "]")
print("       [", arr3[1,0], arr3[1,1], arr3[1,2], "]]")

print("arr3.shape -", arr3.shape)
print("arr3.sum(axis=0) -", arr3.sum(axis=0))
print("arr3.sum(axis=1) -", arr3.sum(axis=1))
print("arr3.sum(axis=2) -", arr3.sum(axis=2))

print("--------------------------AXIS SUM 4D ARRAY---------------------------")
arr4 = np.random.randint(0, 10, (2,2,3,2))
print("arr4", arr4)
print("arr4 =[[[", arr4[0,0,0], arr4[0,0,1], arr4[0,0,2], "][", arr4[0,1,0], arr4[0,1,1], arr4[0,1,2], "]]")
print("        [", arr4[1,0,0], arr4[1,0,1], arr4[1,0,2], "][", arr4[1,1,0], arr4[1,1,1], arr4[1,1,2], "]]]")

print("arr4.shape -", arr4.shape)
print("arr4.sum(axis=0) -", arr4.sum(axis=0))
print("arr4.sum(axis=1) -", arr4.sum(axis=1))
print("arr4.sum(axis=2) -", arr4.sum(axis=2))
print("arr4.sum(axis=3) -", arr4.sum(axis=3))

print("--------------------------AXIS CONCATENATE 3D ARRAY---------------------------")
arr3 = np.random.randint(0, 10, (2,3,2))
print("arr3 =[[", arr3[0,0], arr3[0,1], arr3[0,2], "]")
print("       [", arr3[1,0], arr3[1,1], arr3[1,2], "]]")

arr32 = np.random.randint(0, 10, (2,3,2))
print("arr32 =[[", arr32[0,0], arr32[0,1], arr32[0,2], "]")
print("       [", arr32[1,0], arr32[1,1], arr32[1,2], "]]")

print("np.concatenate(arr3, arr32, axis=0)", np.concatenate((arr3, arr32), axis=0))
print("np.concatenate(arr3, arr32, axis=1)", np.concatenate((arr3, arr32), axis=1))
print("np.concatenate(arr3, arr32, axis=2)", np.concatenate((arr3, arr32), axis=2))

print("--------------------------AXIS CONCATENATE 4D ARRAY---------------------------")
arr4 = np.random.randint(0, 10, (2,2,3,2))
print("arr4", arr4)
arr42 = np.random.randint(0, 10, (2,2,3,2))
print("arr42", arr42)

print("arr4 =[[[", arr4[0,0,0], arr4[0,0,1], arr4[0,0,2], "][", arr4[0,1,0], arr4[0,1,1], arr4[0,1,2], "]]")
print("        [", arr4[1,0,0], arr4[1,0,1], arr4[1,0,2], "][", arr4[1,1,0], arr4[1,1,1], arr4[1,1,2], "]]]")
print("arr42 =[[[", arr42[0,0,0], arr42[0,0,1], arr42[0,0,2], "][", arr42[0,1,0], arr42[0,1,1], arr42[0,1,2], "]]")
print("        [", arr42[1,0,0], arr42[1,0,1], arr42[1,0,2], "][", arr42[1,1,0], arr42[1,1,1], arr42[1,1,2], "]]]")
print("np.concatenate(arr4, arr42, axis=0)", np.concatenate((arr4, arr42), axis=0))

print("arr4 =[[[", arr4[0,0,0], arr4[0,0,1], arr4[0,0,2], "][", arr4[0,1,0], arr4[0,1,1], arr4[0,1,2], "]]")
print("        [", arr4[1,0,0], arr4[1,0,1], arr4[1,0,2], "][", arr4[1,1,0], arr4[1,1,1], arr4[1,1,2], "]]]")
print("arr42 =[[[", arr42[0,0,0], arr42[0,0,1], arr42[0,0,2], "][", arr42[0,1,0], arr42[0,1,1], arr42[0,1,2], "]]")
print("        [", arr42[1,0,0], arr42[1,0,1], arr42[1,0,2], "][", arr42[1,1,0], arr42[1,1,1], arr42[1,1,2], "]]]")
print("np.concatenate(arr4, arr42, axis=1)", np.concatenate((arr4, arr42), axis=1))

print("arr4 =[[[", arr4[0,0,0], arr4[0,0,1], arr4[0,0,2], "][", arr4[0,1,0], arr4[0,1,1], arr4[0,1,2], "]]")
print("        [", arr4[1,0,0], arr4[1,0,1], arr4[1,0,2], "][", arr4[1,1,0], arr4[1,1,1], arr4[1,1,2], "]]]")
print("arr42 =[[[", arr42[0,0,0], arr42[0,0,1], arr42[0,0,2], "][", arr42[0,1,0], arr42[0,1,1], arr42[0,1,2], "]]")
print("        [", arr42[1,0,0], arr42[1,0,1], arr42[1,0,2], "][", arr42[1,1,0], arr42[1,1,1], arr42[1,1,2], "]]]")
print("np.concatenate(arr4, arr42, axis=2)", np.concatenate((arr4, arr42), axis=2))

print("arr4 =[[[", arr4[0,0,0], arr4[0,0,1], arr4[0,0,2], "][", arr4[0,1,0], arr4[0,1,1], arr4[0,1,2], "]]")
print("        [", arr4[1,0,0], arr4[1,0,1], arr4[1,0,2], "][", arr4[1,1,0], arr4[1,1,1], arr4[1,1,2], "]]]")
print("arr42 =[[[", arr42[0,0,0], arr42[0,0,1], arr42[0,0,2], "][", arr42[0,1,0], arr42[0,1,1], arr42[0,1,2], "]]")
print("        [", arr42[1,0,0], arr42[1,0,1], arr42[1,0,2], "][", arr42[1,1,0], arr42[1,1,1], arr42[1,1,2], "]]]")
print("np.concatenate(arr4, arr42, axis=3)", np.concatenate((arr4, arr42), axis=3))

