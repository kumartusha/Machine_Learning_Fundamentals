#  Numpy and its Operations that will be help us in the machine learning model sometime.....

import numpy as np

arr1 = np.array([1,2,3,4,5])

# print(arr1)
# print(np.size(arr1))
# print(np.ndim(arr1))
# print(len(arr1))
# print(np.shape(arr1))
# print(arr1.dtype)
#    Slicing in the numpy array..
# print(arr1[:])
# print(arr1[0:1])
# print(arr1[1:3])
# print(arr1[:2])
# print(arr1[3:])
# print(arr1[-3:-1])


# arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(arr2)
# print(np.size(arr2))
# print(np.shape(arr2))
# print(np.ndim(arr2))
# print(arr2[0:2, 0:2])
# print(arr2[2, 0:3])


# arr3 = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
# print(arr3)
# print(np.size(arr3))
# print(np.ndim(arr3))
# print(np.size(arr3))
# print(len(arr3))

# arr2 = np.append(arr1, [6,7,8,98])
# arr2 = np.insert(arr1, 0, 100)
# arr2 = np.delete(arr1, 4)
# print(arr2)

# arr2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# # arr3 = np.append(arr2, [9,8,7])
# arr3 = np.insert(arr2, 4, [100,101,102])
# print(arr3)

# print(arr2 + arr1)
# print(arr2 - arr1)
# print(arr2 * arr1)
# print(arr2 // arr2)


# print(np.add(arr2, arr1))
# print(np.subtract(arr2, arr1))
# print(np.multiply(arr2, arr1))
# print(np.divide(arr2, arr1))
# print(np.power(arr2, arr1))
# print(np.sqrt(arr2))

# concatenate and the splitting values into the numpy array.
# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,7,8,9,10])
# # 
# arr3 = np.array([[1,2], [3,4]])
# arr4 = np.array([[5,6], [7,8]])

# print(np.concat((arr1, arr2)))
# print(np.concatenate((arr1, arr2)))


# print(np.concatenate((arr3, arr4), axis=0))
# print(np.concatenate((arr3, arr4), axis=1))

# print(np.vstack((arr3, arr4)))
# print(np.hstack((arr3, arr4)))


# arr1 = np.array([1,2,3,4,5])
# print(np.array_split(arr3, 3))
# print(np.shape(arr3))


#  Search filter, searchsorted, sort
arr1 = np.array([10,4,3,2,1])
# print(np.sort(arr1))
# new_ar = np.where(arr1 < 5)
# print(new_ar[0][1] > 4)
# print(np.searchsorted(arr1, 3))

# print(np.searchsorted(arr1, [6,8]))

# import numpy as np

# Sorted array
# arr = np.array([1,2 ,3,4,5,6,7])

# # Find positions for the value(s)
# result = np.searchsorted(arr, [4, 6])
# print(result) 


# Aggregate functions in the numpy array.

# arr1 = np.array([1,2,3,4])
# print(np.sum(arr1))
# print(np.min(arr1))
# print(np.max(arr1))
# print(int(np.mean(arr1)))
# print(int(np.median(arr1)))
# print(np.size(arr1))
# print(np.mean(arr1))
# print(np.cumsum(arr1))
# print(np.cumprod(arr1))


# arr1 = [1,2,3,4,5,6]
# arr2 = [100,200,300,400,500,600]

# quantity = np.array(arr1)
# price = np.array(arr2)

# result = np.cumprod([price, quantity], axis=0)
# result2 = np.cumprod([price, quantity], axis=1)
# print(result)
# print(result2)

# arr1 = [1,2,3,4,5]

# print(np.mean(arr1))
# print(np.median(arr1))
# print(np.cumprod(arr1))
# print(np.cumsum(arr1))

# names = ["tushar", "tushar", "rak", "rak", "shi", "ank", "komal", "lalit"]

# print(np.mod(names))
# print(np.unique(names))


# Task Given Solutions of the numpy..
# arr1 = []
# for i in range(100):
#    arr1.append(np.random.randint(100))

# # print(len(arr1))
# print(np.mean(arr1))
# print(np.median(arr1))
# print(np.std(arr1))
# print(np.var(arr1))

# arr1 = np.array([1,2,3,4,5,6,7,8])
# arr2 = arr1.reshape(2,2,2)
# print(arr2)


# arr1 = np.array([[[1,2], [3,4]], [[5,6],[7,8]]])
# print(arr1)

# arr1 = np.array([[[[1,2], [3,4]], [[5,6],[7,8]]], [[[1,2], [3,4]], [[5,6],[7,8]]]])
# print(arr1)

# print(arr1.ndim)

# arr1 = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

# print(arr1[0:3, 0:3])

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.array([6,7,8,9,10])

# print(np.cross(arr1, arr2))

# arr1 = np.array([1,2,3,4,5,6])

# for i in range(len(arr1)):
#     if arr1[i] % 2 == 0:
#         arr1[i] = -1

# print(arr1)

# print(np.argmax(arr1))
# print(np.argmin(arr1))

# arr1 = np.array([5,43,2,1])
# print(np.sort(arr1))

# arr1 = []

# for i in range(100):
#     arr1.append(np.random.randint(1,100))

# print(arr1)
# print(len(arr1))
# print(np.unique(arr1))
# print(len(np.unique(arr1)))

# arr1 = np.array([[1,2], [3,4]])
# arr2 = np.array([[5,6], [7,8]])

# print(np.dot(arr1, arr2))

# arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
# print(np.array_split(arr1, 3))

arr1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(np.transpose(arr1))
# print(np.invert(arr1))

# print(np.round(464.38))
# arr1[2][1] = 6767
# print(np.ravel(arr1))
# # print(arr1.flatten())

# print(arr1)

# ravel_arr = np.ravel(arr1)
# ravel_arr[0] = 376 
# print(ravel_arr)
# print(arr1)

# flaten_arr = arr1.ravel()
# print(flaten_arr)
# flaten_arr[0] = 376 
# print(arr1)

arr = np.array([[1, 2, 3], [4, 5, 6]])

# flattend = arr.flatten()
# print(flattend)

# flattend[0] = 657

# print(flattend)
# print(arr)

# raveli = np.ravel(arr)
# print(raveli)

# raveli[0] = 657

# print(raveli)
# print(arr)


# def sum(x):
#     return x + 50

# arr1 = np.array([1,2,3,4,5])

# vectorize_arr = np.vectorize(sum)

# result = vectorize_arr(arr1)

# print(result)

# arr1 = np.array([10,20,30,40,50])

# clipped_arr = np.clip(arr1, 5,15)
# print(clipped_arr)


