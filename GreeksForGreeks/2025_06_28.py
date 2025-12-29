def permutation():
    arr: list[int] = [2,3,1,6,5]
    n: int = len(arr)
    pivot: int = -1

    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            pivot = i
            break

    if pivot == -1:
        arr.reverse()
        
    for i in range(n-1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    left, right = pivot+1, n-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        right -= 1
        left +=1
    print(arr)