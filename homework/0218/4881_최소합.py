def backtrack(idx, total):
    global min_sum

    if total >= min_sum:
        return

    if idx == N:
        min_sum = min(min_sum, total)
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            backtrack(idx+1, total+arr[idx][col])
            visited[col] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_sum = 10**10
    backtrack(0, 0)
    print(f'#{tc} {min_sum}')