T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    middle = N // 2
    result = 0

    # 위 삼각형
    for i in range(middle+1):
        start = middle - i
        end = middle + i
        for c in range(start, end+1):
            result += farm[i][c]

    # 아래 삼각형
    for i in range(middle+1, N):
        start = middle - (N-1-i)
        end = middle + (N-1-i)
        for c in range(start, end+1):
            result += farm[i][c]

    print(f'#{tc} {result}')
