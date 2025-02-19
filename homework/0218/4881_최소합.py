def backtrack(idx):
    if idx == N:
        res.append(arr)
        return
    else:
        for i in range(N):
            if not

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    res = []
    backtrack(N)

