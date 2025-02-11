T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    string = [input() for _ in range(N)]
    result = 0

    # 가로줄
    for i in range(N):       # 행
        for j in range(N-M+1):   # 시작 지점
            for k in range(M//2):
                if string[i][j+k] != string[i][j+M-1-k]:
                    break
            else:
                result = string[i][j:j+M]

    #  세로줄
    for c in range(N):
        for r in range(N-M+1):
            for k in range(M//2):
                if string[r+k][c] != string[r+M-1-k][c]:
                    break
            else:
                result = ''.join(string[r+x][c] for x in range(M))

    print(f'#{tc} {result}')

