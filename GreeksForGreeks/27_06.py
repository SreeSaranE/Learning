def rev():
    arr = [1, 4, 3, 2, 6, 5]
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    print(arr)

def rotateArr():
    arr = [1, 2, 3, 4, 5]
    d = 2
    len_arr = len(arr)
    d = d % len_arr
    reverse(arr, 0, d-1)
    reverse(arr, d, len_arr-1)
    reverse(arr, 0, len_arr-1)
    print(arr)
def reverse(arr, start, end):
    while start< end:
        arr[start] , arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
