def special_sort(arr, n):
    for i in range(n-1):
        max_idx, min_idx = i, i
        for j in range(i, n):
            if i % 2 == 0:
                if arr[max_idx] < arr[j]:
                    max_idx = j
            else:
                if arr[min_idx] > arr[j]:
                    min_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return ' '.join(map(str, arr[:10]))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {special_sort(arr, N)}')
