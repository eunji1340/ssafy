T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[1] for _ in range(N)]

    for i in range(1, N):
        for j in range(1, i+1):
            if j == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i-1][j-1] + arr[i-1][j])

    print(f'#{tc}')
    for row in arr:
        print(' '.join(map(str, row)))