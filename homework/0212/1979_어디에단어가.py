def find_position(n, K, arr):
    ct = 0

    # 가로
    for i in range(n):
        for j in range(n-K+1):
            if arr[i][j] == 1 and (j == 0 or arr[i][j-1] == 0):
                for k in range(1, K):
                    if arr[i][j+k] != 1:
                        break
                else:
                    if j+K == n or arr[i][j+K] == 0:
                        ct += 1

    # 세로
    for j in range(n):
        for i in range(n-K+1):
            if arr[i][j] == 1 and (i == 0 or arr[i-1][j] == 0):
                for k in range(1, K):
                    if arr[i+k][j] != 1:
                        break
                else:
                    if i+K == n or arr[i+K][j] == 0:
                        ct += 1
    return ct

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {find_position(N, K, puzzle)}')