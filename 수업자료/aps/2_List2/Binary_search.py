def binary_search(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start+end)//2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1

arr = [4, 9, 11, 23, 2, 19, 7]
arr.sort()
print(arr)
print(binary_search(arr, len(arr), 11))
print(binary_search(arr, len(arr), 7))