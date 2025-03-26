T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j = 0, 0
    d = 0
    num = 1

    while num <= N*N:
        arr[i][j] = num
        num += 1

        ni = i + di[d]
        nj = j + dj[d]

        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            d = (d + 1) % 4
            ni = i + di[d]
            nj = j + dj[d]

        i = ni
        j = nj

    print(f'#{tc}')
    for row in arr:
        print(*row)
