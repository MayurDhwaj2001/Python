from numpy import *

array1 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

array1d = array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

print(array1)
print(array1.flatten())
array2d = array1d.reshape(3, 4)
print(array2d)
print("\n")
array3d = array1d.reshape(2, 2, 3)
print(array3d)
