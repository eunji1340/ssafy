T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0

    for R in range(N-M+1):
        for C in range(N-M+1):
            cnt = 0
            for r in range(M):
                for c in range(M):
                    cnt += arr[R+r][C+c]

            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')