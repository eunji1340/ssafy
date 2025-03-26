def sort_arr(arr, n):
    sort_arr = []
    for row in arr:
        for elem in row:
            sort_arr.append(elem)

    for i in range(n*n-1):
        min_idx = i
        for j in range(i+1, n*n):
            if sort_arr[min_idx] > sort_arr[j]:
                min_idx = j
        sort_arr[min_idx], sort_arr[i] = sort_arr[i], sort_arr[min_idx]

    return sort_arr

def dalpang(arr, n):
    result = [[0] * n for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(n):
        for j in range(n):
            d = 0
            while (0<=i+di<n) and (0<=j+dj<n):
                result[i+di[0]][j+dj[0]] = arr[i][j]

T = int(input())

for tc in range(1, T+1):
    n = int(input())  # n*n 배열
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(dalpang(sort_arr(arr, n)), n)


