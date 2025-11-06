import numpy as np

'''
arr = np.arange(10)
arr_slice = arr[3:6].copy()
print (arr, '\n', arr_slice)

arr_slice[0] = 20
print (arr, '\n', arr_slice)
'''

arr1: list[int] = list(range(1,11))
arr2: list[int] = list(range(11,21))

rev: slice = slice(None, None, -1)
first_5: slice  = slice(None, 5, None) # (0,5)
print(arr1[rev])
print(arr2[first_5])