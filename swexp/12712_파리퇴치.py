T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ct = 0

    for r in range(N):
        for c in range(N):
            temp = arr[r][c]
            for dr, dc in [[0,1], [-1,0], [0,-1], [1,0]]:
                for m in range(1, M):
                    nr = r + dr * m
                    nc = c + dc * m
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            ct = max(ct, temp)

            temp = arr[r][c]
            for dr, dc in [[1,1], [-1,1], [-1,-1], [1,-1]]:
                for m in range(1, M):
                    nr = r + dr * m
                    nc = c + dc * m
                    if 0 <= nr < N and 0 <= nc < N:
                        temp += arr[nr][nc]
            ct = max(ct, temp)

    print(f'#{tc} {ct}')