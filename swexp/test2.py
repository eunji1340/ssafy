T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [[0] * N for _ in range(4)]

    for k in range(1, K+1):
        for i in range(4):
            for j in range(N):
                if (i+j+1) % k == 0:
                    board[i][j] = (board[i][j] + 1) % 2

    ct = 0
    for i in range(4):
        for j in range(N):
            if board[i][j] == 1:
                ct += 1

    print(f'#{tc} {ct}')