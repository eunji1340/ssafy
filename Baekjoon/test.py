T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    # 가로 확인
    for r in range(N):
        for c in range(N-K+1):
            if sum(puzzle[r][c:c+K]) == K and (c+K == N or puzzle[r][c+K] == 0):
                result += 1

    print(f'#{tc} {result}')