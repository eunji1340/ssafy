dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

dr2 = [-1, -1, 1, 1]
dc2 = [1, -1, 1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    for r in range(N):
        for c in range(N):
            # 가로, 세로
            temp = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr[d]*m
                    nc = c + dc[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            Max = max(Max, temp)

            # 대각선
            temp = arr[r][c]
            for d in range(4):
                for m in range(1, M):
                    nr = r + dr2[d]*m
                    nc = c + dc2[d]*m
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            Max = max(Max, temp)

    print(f'#{tc} {Max}')