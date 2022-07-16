import numpy as np
# tested on numpy==1.22.1
# https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
print(np.__version__)


zeros1 = np.zeros(shape=(1,2,3), dtype=np.float32)
print("zeros1 = ", zeros1)
ones1 = np.ones(shape=(3,2,1), dtype=int)
print("ones1 = ", ones1)
empty1 = np.empty(shape=(2,1, 3), dtype=int)
print("empty1 = ", empty1)
full1 = np.full(fill_value=96.3, shape=(2,1, 3), dtype=float)
print("full1 = ", full1)
print("ones1 like full1", np.ones_like(full1))
print("----------------------------------------------------------------")
print("arange", np.arange(2,18,2))
print("linspace", np.linspace(2.0,18.0,3))
print("randint", np.random.randint(5,15,4))
print("randint of given shape", np.random.randint(5,15,(2,1,2)))
print("rand", np.random.rand(2,1,2)) # create array of random floating numbers 0-1 of given shape 
print("uniform - ", np.random.uniform(5,15,4))
print("uniform of given shape -", np.random.uniform(5,15,(1,2,1)))

print("--------------NUMPY INDEXING---------------------------------------")
arr1 = np.arange(17, 27)
print("arr1 =", arr1, "shape =", arr1.shape)
print("slicing", arr1[2:6])
print("slicing out of bounds", arr1[2:20:2])
print("negative slicing out of bounds", arr1[30:2:-2])
print("negative indexing", arr1[-8:-2])
print("step only", arr1[::3])
print("fancy indexing", arr1[[2,3,4,7,8]])

print("---------------------REPLACING ELEMS-----------------")
arr1[3:5] = 97
print("replace elems of multple indices by single value", arr1)
arr1[7:9] = [47, 56]
print("replace elems of multple indices by multiple values", arr1)

print("---------------------BOOLEAN OPERATIONS---------------")
print("remove elems using conditions", arr1[arr1%2==1])
print("np.any -", np.any(arr1 > 20))
print("np.all -", np.all(arr1 < 0))
print("AND operation", arr1[(arr1%2==0) & (arr1>=22)])
print("OR operation", arr1[(arr1%2==0) | (arr1>=50)])

print("---------------------MATHEMATICAL OPERATIONS---------------")
print("sine pi/6, pi/4, pi/3, pi/2 -", np.sin([np.pi/6, np.pi/4, np.pi/3, np.pi/2])) # Radians
print("Inverse sine ", np.arcsin([0.5, 0.70710678, 0.8660254, 1.0])) # Radians
# arcsin is a multivalued function. For each x there are infinitely many numbers z such that sin(x)=z. The convention is to return the angle z whose real part lies in [-pi/2, pi/2]
print("hypot function ", np.hypot(3*np.ones((3, 3)), 4*np.ones((3, 3))))
# Pythogoras Theorem. Given the “legs” of a right triangle, return its hypotenuse.
print("arr1 =", arr1)
print("arr1.max() -", arr1.max())
print("index of max element, arr.argmax() -", arr1.argmax())
print("arr1.min() -", arr1.min())
print("index of min element, arr.argmin() -", arr1.argmin())
print("sum of array, arr.sum()", arr1.sum())
print("variance of array elements, arr.var()", arr1.var())
print("mean of array, arr.mean()", arr1.mean())
print("standard deviation of array elements, arr.std()", arr1.std())

print("arr1 =", arr1)
print("sort the array and return index of a element", np.searchsorted(arr1, 47))
print("like sorted method of python", np.sort(arr1))
print("like sort method, arr.sort() returns", arr1.sort(), "but sorts the array itself")


