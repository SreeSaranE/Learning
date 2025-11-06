def second_max():
    Input1 = [12, 35, 1, 10, 34, 1]
    max_val = memeory = -1
    for i in Input1:
        if i > max_val:
            memeory = max_val
            max_val = i
        elif i < max_val and i > memeory:
            memeory = i
    print(memeory)

def pushZerosToEnd():
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] , arr[i]= arr[i], arr[count]
            count += 1
    print(arr)
