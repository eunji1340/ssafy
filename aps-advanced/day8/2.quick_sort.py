def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

def partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]



arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]