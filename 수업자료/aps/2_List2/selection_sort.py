def selection_sort(a, n):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

arr = [4, 9, 11, 23, 2, 19, 7]
print(selection_sort(arr, len(arr)))
