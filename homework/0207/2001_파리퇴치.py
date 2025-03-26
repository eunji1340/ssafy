T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = 0

    for R in range(N-M+1):
        for C in range(N-M+1):
            temp = 0
            for r in range(M):
                for c in range(M):
                    temp += arr[R+r][C+c]
            Max = max(Max, temp)

    print(f'#{tc} {Max}')