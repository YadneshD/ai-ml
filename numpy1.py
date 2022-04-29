import numpy as np
# numpy==1.22.1
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
print("np.all -", np.any(arr1 < 0))



