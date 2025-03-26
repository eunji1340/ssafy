T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    result = [''] * N

    # 90도
    for c in range(N):
        for r in range(N-1, -1, -1):
            result[c] += arr[r][c]
        result[c] += ' '

    # 180도
    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            result[N-r-1] += arr[r][c]
        result[N-r-1] += ' '

    # 270도
    for c in range(N-1, -1, -1):
        for r in range(N):
            result[N-c-1] += arr[r][c]

    print(f'#{tc}')
    for row in result:
        print(row)