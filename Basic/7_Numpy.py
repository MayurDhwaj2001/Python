# Used while creating multi dimensional array
from statistics import mode

from numpy import *

arra = array([1, 2, 3, 4, 5, 5], int)
ran = arange(2, 21, 2)
zero = zeros(6)
one = ones(5, int)

print(arra)
print("even numbers", ran)
print(zero)
print(one)

# operations in array
arr = array([1, 7, 2, 5, 8, 22, 4, 2, 5, 2])
arr2 = array([4, 2, 7, 77, 21, 2])
print("min", min(arr))
print('max', max(arr))
print('sum', sum(arr))
print('sort', sort(arr))
print('mean', mean(arr))
print('median', median(arr2))
print('mode', mode(arr))  # import statistics
print('Concatination', concatenate([arr, arr2]))

# Shallow Copy & Deep Copy
# Shallow Copy - Copies the array in  different address but value changes according to first array
#     array2=array1.view()
array1 = arr.view()
arr[0] = 9
print("arr", arr)
print("array1", array1)

# Deep Copy - Copies the array in  different address and value are independent
#     array2=array1.copy()
array2 = arr.copy()
arr[0] = 5
print("arr", arr)
print("array2", array2)
