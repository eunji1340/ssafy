T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0
    mid = N // 2

    for i in range(N):
        if i <= mid:
            for j in range(mid - i, mid + i + 1):
                result += farm[i][j]
        else:
            for j in range(i - mid, N - i + mid):
                result += farm[i][j]

    print(f'#{tc} {result}')